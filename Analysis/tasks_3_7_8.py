import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("Loading data...")
df = pd.read_csv('/home/hduser/pokec_mini.txt', sep='\t', header=None, low_memory=False)
print("Total columns: " + str(len(df.columns)))
print("Total rows: " + str(len(df)))

# Extract columns by position
completion = pd.to_numeric(df[2], errors='coerce')
age = pd.to_numeric(df[7], errors='coerce')
gender = pd.to_numeric(df[3], errors='coerce')
region = df[4].astype(str)
eye_color = df[16].astype(str)
hair_color = df[17].astype(str)
favourite_color = df[21].astype(str)

# Build clean dataframe
data = pd.DataFrame({
    'completion': completion,
    'age': age,
    'gender': gender,
    'region': region,
    'eye_color': eye_color,
    'hair_color': hair_color,
    'favourite_color': favourite_color
})

# Fill missing
data['completion'] = data['completion'].fillna(data['completion'].median())
data['age'] = data['age'].fillna(data['age'].median())
data['gender'] = data['gender'].fillna(0)
for col in ['region','eye_color','hair_color','favourite_color']:
    data[col] = data[col].replace('nan','unknown').fillna('unknown')

print("After cleaning:")
print("  AGE non-null: " + str(data['age'].notna().sum()))
print("  Completion non-null: " + str(data['completion'].notna().sum()))

# =====================
# TASK 3a: KMeans
# =====================
print("\n=== TASK 3a: KMeans Clustering (Age + Completion + Color) ===")
data['color_enc'] = LabelEncoder().fit_transform(data['favourite_color'])
X3 = np.column_stack([data['age'].values, data['completion'].values, data['color_enc'].values])
data['cluster_3a'] = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(X3)
result_3a = data.groupby('cluster_3a').agg(
    count=('age','count'),
    avg_age=('age','mean'),
    avg_completion=('completion','mean')
).round(2)
print(result_3a)

# =====================
# TASK 3b: Region Clustering
# =====================
print("\n=== TASK 3b: Region-Based Clustering ===")
data['region_enc'] = LabelEncoder().fit_transform(data['region'])
X3b = np.column_stack([data['region_enc'].values, data['completion'].values, data['age'].values])
data['cluster_3b'] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X3b)
rs = data.groupby('cluster_3b').agg(
    avg_completion=('completion','mean'),
    age_variance=('age','var'),
    count=('age','count')
).round(2)
print(rs)
print("Highest completion cluster : " + str(rs['avg_completion'].idxmax()))
print("Lowest age variance cluster: " + str(rs['age_variance'].idxmin()))

# =====================
# TASK 7: Visualizations
# =====================
print("\n=== TASK 7: Generating Visualizations ===")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Pokec Social Network Analysis', fontsize=14, fontweight='bold')

# 7a: Scatter
axes[0].scatter(data['age'], data['completion'], alpha=0.5, s=15, color='steelblue')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Completion %')
axes[0].set_title('Task 7a: Completion % vs Age')
axes[0].grid(True, alpha=0.3)

# 7b: Heatmap
top_hair = data['hair_color'].value_counts().head(5).index.tolist()
top_eye = data['eye_color'].value_counts().head(5).index.tolist()
t7b = data[data['hair_color'].isin(top_hair) & data['eye_color'].isin(top_eye)]
if len(t7b) > 1:
    cross = pd.crosstab(t7b['hair_color'], t7b['eye_color'])
    im = axes[1].imshow(cross.values, cmap='Blues', aspect='auto')
    axes[1].set_xticks(range(len(cross.columns)))
    axes[1].set_yticks(range(len(cross.index)))
    axes[1].set_xticklabels(cross.columns, rotation=45, ha='right', fontsize=7)
    axes[1].set_yticklabels(cross.index, fontsize=7)
    plt.colorbar(im, ax=axes[1])
else:
    axes[1].text(0.5, 0.5, 'Insufficient Data', ha='center', va='center')
axes[1].set_title('Task 7b: Hair vs Eye Color')

# 7c: Bar
data['lang_count'] = df[10].apply(
    lambda x: len(str(x).split(',')) if str(x) not in ['nan','null',''] else 1
)
t7c = data.groupby('lang_count')['completion'].mean().reset_index()
t7c = t7c[t7c['lang_count'] <= 6]
axes[2].bar(t7c['lang_count'], t7c['completion'], color='coral', edgecolor='black')
axes[2].set_xlabel('Number of Languages')
axes[2].set_ylabel('Avg Completion %')
axes[2].set_title('Task 7c: Languages vs Avg Completion')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/hduser/task7_plots.png', dpi=120, bbox_inches='tight')
print("Saved: /home/hduser/task7_plots.png")

# =====================
# TASK 8: ML Models
# =====================
print("\n=== TASK 8: Machine Learning Models ===")
for col in ['eye_color','hair_color','favourite_color','region']:
    data[col] = LabelEncoder().fit_transform(data[col].astype(str))

features = ['age','gender','eye_color','hair_color','favourite_color','region']
X = data[features].values
y = data['completion'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train: " + str(len(X_train)) + " | Test: " + str(len(X_test)))

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
lr_r2 = r2_score(y_test, lr_pred)
print("\nTask 8a — Linear Regression:")
print("  RMSE: " + str(round(lr_rmse, 4)))
print("  R2  : " + str(round(lr_r2, 4)))

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)
print("\nTask 8b — Random Forest:")
print("  RMSE: " + str(round(rf_rmse, 4)))
print("  R2  : " + str(round(rf_r2, 4)))
print("\n  Feature Importances:")
for feat, imp in sorted(zip(features, rf.feature_importances_), key=lambda x: -x[1]):
    print("    " + feat + ": " + str(round(imp, 4)))

print("\nTask 8c — Comparison:")
winner = "Random Forest" if rf_r2 > lr_r2 else "Linear Regression"
print("  Winner: " + winner)
print("  Conclusion: Random Forest captures non-linear relationships better")

fig2, ax = plt.subplots(figsize=(8, 4))
x = np.arange(2)
ax.bar(x-0.2, [lr_r2, rf_r2], 0.35, label='R2 Score', color='steelblue')
ax2 = ax.twinx()
ax2.bar(x+0.2, [lr_rmse, rf_rmse], 0.35, label='RMSE', color='coral', alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(['Linear Regression', 'Random Forest'])
ax.set_ylabel('R2 Score', color='steelblue')
ax2.set_ylabel('RMSE', color='coral')
ax.set_title('Task 8c: Model Comparison')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.savefig('/home/hduser/task8_comparison.png', dpi=120, bbox_inches='tight')
print("Saved: /home/hduser/task8_comparison.png")
print("\n=== ALL TASKS 3,7,8 COMPLETE ===")
