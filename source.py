import pandas as pd
df = pd.read_csv('MetObjects.csv')
df.shape
#removing unnecessary fields for this investigation
new_df = df.drop(columns=['Is Timeline Work', 'Is Public Domain', 'Rights and Reproduction', 'Object Wikidata URL', 'Metadata Date', 'Repository', 'Tags AAT URL', 'Tags Wikidata URL', 'AccessionYear', 'Subregion', 'Locale', 'Locus', 'River', 'Dynasty', 'Geography Type', 'City', 'Gallery Number', 'Period', 
                'State', 'County', 'Reign', 'Object End Date', 'Dimensions', 'Credit Line', 'Region', 'Excavation', 'Object Begin Date', 'Artist Wikidata URL', 'Artist ULAN URL', 'Portfolio', 'Constituent ID', 'Artist End Date', 'Object Name', 'Artist Prefix', 'Artist Role', 'Artist Display Bio', 'Artist Alpha Sort', 'Artist Suffix'])
new_df.isnull().sum()
new_df['Artist Display Name'].value_counts()
new_df['Artist Nationality'].value_counts()
new_df['Artist Gender'].value_counts()
new_df['Is Highlight'].value_counts()
new_df['Department'].value_counts()
new_df['Culture'].value_counts()
new_df['Classification'].value_counts().nlargest(20)
highlights_df = new_df[new_df['Is Highlight'] == True]
highlights_df.shape
highlights_df.isnull().sum()
highlights_df['Artist Display Name'].value_counts()
highlights_df['Artist Nationality'].value_counts()
highlights_df['Department'].value_counts()
highlights_df['Classification'].value_counts()
American_df = new_df[new_df['Department'] == 'The American Wing']
American_df.shape
American_df.head()
American_df['Medium'].value_counts()
highlights_df['Medium'].value_counts()
oil_df = new_df[new_df['Medium'] == 'Oil on canvas']
oil_df.shape
