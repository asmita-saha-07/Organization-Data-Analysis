import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("organizations-100.csv")
df=pd.DataFrame(data)

df.dropna(inplace=True)

plt.figure(figsize=(22,10))

current_year=2026
oldest_organizations=df.sort_values(by='Founded',ascending=True).head(10)
top_companies=df.sort_values(by='Number of employees', ascending=False).head(10)
top_countries=df['Country'].value_counts().head(10)
youngest_organizations=df.sort_values(by='Founded',ascending=False).head(10)

plt.subplot(2,2,1)
plt.bar(oldest_organizations['Name'],current_year - oldest_organizations['Founded'],color='red')
plt.xlabel('Organization Names')
plt.ylabel('Organization Age')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.title('Oldest Organizations')

plt.subplot(2,2,2)
plt.bar(youngest_organizations['Name'],current_year - youngest_organizations['Founded'],color='blue')
plt.xlabel('Organization Names')
plt.ylabel('Organization Age')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.title('Youngest Organizations')

plt.subplot(2,2,3)
plt.bar(top_companies['Name'],top_companies['Number of employees'], color='green')
plt.xlabel('Organization Names')
plt.ylabel('Number of employees')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.title('Top Companies')

plt.subplot(2,2,4)
plt.bar(top_countries.index,top_countries.values, color='yellow')
plt.xlabel('Country names')
plt.ylabel('Number of Organizations')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.title('Top Countries')


plt.tight_layout(pad=5.0)
plt.show()