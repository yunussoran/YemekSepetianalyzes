
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('/Users/berrenurerdogan/PycharmProjects/YemekSepetiAnalyzes/data/task1-dataset-1723704917.xlsx', sheet_name='orders_detailed')






total_orders = len(df)
contact_rate = df['isContact'].mean() * 100
self_service_rate = df['isSelfService'].mean() * 100
seamless_order_rate = df['isSeamless'].mean() * 100
nps_average = df['NPS-Q-Score'].mean()
contact_csat_average = df[df['isContact'] == 1]['ContactCSAT'].mean()
self_service_csat_average = df[df['isSelfService'] == 1]['SelfServiceCSAT'].mean()


print(f"Total Orders: {total_orders}")
print(f"Contact Rate: {contact_rate:.2f}%")
print(f"Self-Service Rate: {self_service_rate:.2f}%")
print(f"Seamless Order Rate: {seamless_order_rate:.2f}%")
print(f"Average NPS Score: {nps_average:.2f}")
print(f"Average Contact CSAT: {contact_csat_average:.2f}")
print(f"Average Self-Service CSAT: {self_service_csat_average:.2f}")


self_service_orders = df[df['isSelfService'] == 1]
self_service_nps = self_service_orders['NPS-Q-Score'].mean()
self_service_csat = self_service_orders['SelfServiceCSAT'].mean()

print(f"\
Self-Service Channel Analysis:")
print(f"Average NPS Score for Self-Service: {self_service_nps:.2f}")
print(f"Average CSAT for Self-Service: {self_service_csat:.2f}")


correlation_matrix = self_service_orders[['order_size_TRY', 'SelfServiceCSAT', 'NPS-Q-Score']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix for Self-Service Orders')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=self_service_orders, x='order_size_TRY', y='SelfServiceCSAT')
plt.title('Order Size vs Self-Service CSAT')
plt.xlabel('Order Size (TRY)')
plt.ylabel('Self-Service CSAT')
plt.tight_layout()
plt.savefig('order_size_vs_csat.png')
plt.close()

payment_method_satisfaction = self_service_orders.groupby('preffered_payment_method')['SelfServiceCSAT'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
payment_method_satisfaction.plot(kind='bar')
plt.title('Average Self-Service CSAT by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Average CSAT')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('csat_by_payment_method.png')
plt.close()

print("\
Analysis complete.")