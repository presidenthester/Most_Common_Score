import pandas as pd




class ScoreFormat():
    def __init__(self):
        pass
        
    def format_score_year(self, file):
        self.csv_file = file
        self.merged_year = pd.read_csv(self.csv_file)  # Read the CSV file into DataFrame
        
        # Fill non-finite values with 0 and convert 'Pts' and 'Pts.1' columns to integers
        self.merged_year['Pts'] = self.merged_year['Pts'].fillna(0).astype(int)
        self.merged_year['Pts.1'] = self.merged_year['Pts.1'].fillna(0).astype(int)

        # Combine 'Pts' and 'Pts.1' columns with a '-' in between
        self.merged_year['Combined_Pts'] = self.merged_year['Pts'].astype(str) + '  -  ' + self.merged_year['Pts.1'].astype(str)

        # Drop the original 'Pts' and 'Pts.1' columns, as they are no longer needed
        self.merged_year.drop(columns=['Pts', 'Pts.1'], inplace=True)

        filename_part = self.csv_file.split("\\")[-1].split(".")[0]
        new_filename = f'{filename_part}_merged.csv'

        # Save the DataFrame to the new file
        self.merged_year.to_csv(f'D:\\MostCommonScore\\Merged_CSVs\\{new_filename}', index=False)
        
        value_counts = self.merged_year['Combined_Pts'].value_counts().reset_index()
        value_counts.columns = ['Score', 'Count']
        
        self.sorted_value_counts = value_counts.sort_values(by='Count', ascending=False)

        #print(sorted_value_counts)
        
        # To use sorted_value_counts: obj.sorted_calue_counts
        
    def all_years(self):
        self.all_year_scores = pd.read_csv(r"D:\\MostCommonScore\\Merged_CSVs\\merge-csv.com__64cc71a569499.csv")
        self.all_year_scores.drop(columns=['Week','Day','Date','Time','Winner/tie','Unnamed: 5','Loser/tie','Unnamed: 7','YdsW','TOW','YdsL','TOL'], inplace=True)
        value_counts = self.all_year_scores['Combined_Pts'].value_counts().reset_index()
        value_counts.columns = ['Score', 'Count']
        self.sorted_value_counts = value_counts.sort_values(by='Count', ascending=False)
        
    
    



# Create objects for each csv.
# Create new csvs with formatted score
# These are created seperatley to keep the originals intact
# Every year and decade will be shown individually, as well as an All Time list made up from all files

# 1960's
sea_1966_AFL = ScoreFormat()
sea_1966_AFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1966AFL.csv")

sea_1967_AFL = ScoreFormat()
sea_1967_AFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1967AFL.csv")

sea_1968_AFL = ScoreFormat()
sea_1968_AFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1968AFL.csv")

sea_1969_AFL = ScoreFormat()
sea_1969_AFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1969AFL.csv")

sea_1966_NFL = ScoreFormat()
sea_1966_NFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1966NFL.csv")

sea_1967_NFL = ScoreFormat()
sea_1967_NFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1967NFL.csv")

sea_1968_NFL = ScoreFormat()
sea_1968_NFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1968NFL.csv")

sea_1969_NFL = ScoreFormat()
sea_1969_NFL.format_score_year(r"D:\\MostCommonScore\\CSVs\\1969NFL.csv")

# 1970's
sea_70 = ScoreFormat()
sea_70.format_score_year(r"D:\\MostCommonScore\\CSVs\\1970.csv")

sea_71 = ScoreFormat()
sea_71.format_score_year(r"D:\\MostCommonScore\\CSVs\\1971.csv")

sea_72 = ScoreFormat()
sea_72.format_score_year(r"D:\\MostCommonScore\\CSVs\\1972.csv")

sea_73 = ScoreFormat()
sea_73.format_score_year(r"D:\\MostCommonScore\\CSVs\\1973.csv")

sea_74 = ScoreFormat()
sea_74.format_score_year(r"D:\\MostCommonScore\\CSVs\\1974.csv")

sea_75 = ScoreFormat()
sea_75.format_score_year(r"D:\\MostCommonScore\\CSVs\\1975.csv")

sea_76 = ScoreFormat()
sea_76.format_score_year(r"D:\\MostCommonScore\\CSVs\\1976.csv")

sea_77 = ScoreFormat()
sea_77.format_score_year(r"D:\\MostCommonScore\\CSVs\\1977.csv")

sea_78 = ScoreFormat()
sea_78.format_score_year(r"D:\\MostCommonScore\\CSVs\\1978.csv")

sea_79 = ScoreFormat()
sea_79.format_score_year(r"D:\\MostCommonScore\\CSVs\\1979.csv")

# 1980's
sea_80 = ScoreFormat()
sea_80.format_score_year(r"D:\\MostCommonScore\\CSVs\\1980.csv")

sea_81 = ScoreFormat()
sea_81.format_score_year(r"D:\\MostCommonScore\\CSVs\\1981.csv")

sea_82 = ScoreFormat()
sea_82.format_score_year(r"D:\\MostCommonScore\\CSVs\\1982.csv")

sea_83 = ScoreFormat()
sea_83.format_score_year(r"D:\\MostCommonScore\\CSVs\\1983.csv")

sea_84 = ScoreFormat()
sea_84.format_score_year(r"D:\\MostCommonScore\\CSVs\\1984.csv")

sea_85 = ScoreFormat()
sea_85.format_score_year(r"D:\\MostCommonScore\\CSVs\\1985.csv")

sea_86 = ScoreFormat()
sea_86.format_score_year(r"D:\\MostCommonScore\\CSVs\\1986.csv")

sea_87 = ScoreFormat()
sea_87.format_score_year(r"D:\\MostCommonScore\\CSVs\\1987.csv")

sea_88 = ScoreFormat()
sea_88.format_score_year(r"D:\\MostCommonScore\\CSVs\\1988.csv")

sea_89 = ScoreFormat()
sea_89.format_score_year(r"D:\\MostCommonScore\\CSVs\\1989.csv")


# 1990's
sea_90 = ScoreFormat()
sea_90.format_score_year(r"D:\\MostCommonScore\\CSVs\\1990.csv")

sea_91 = ScoreFormat()
sea_91.format_score_year(r"D:\\MostCommonScore\\CSVs\\1991.csv")

sea_92 = ScoreFormat()
sea_92.format_score_year(r"D:\\MostCommonScore\\CSVs\\1992.csv")

sea_93 = ScoreFormat()
sea_93.format_score_year(r"D:\\MostCommonScore\\CSVs\\1993.csv")

sea_94 = ScoreFormat()
sea_94.format_score_year(r"D:\\MostCommonScore\\CSVs\\1994.csv")

sea_95 = ScoreFormat()
sea_95.format_score_year(r"D:\\MostCommonScore\\CSVs\\1995.csv")

sea_96 = ScoreFormat()
sea_96.format_score_year(r"D:\\MostCommonScore\\CSVs\\1996.csv")

sea_97 = ScoreFormat()
sea_97.format_score_year(r"D:\\MostCommonScore\\CSVs\\1997.csv")

sea_98 = ScoreFormat()
sea_98.format_score_year(r"D:\\MostCommonScore\\CSVs\\1998.csv")

sea_99 = ScoreFormat()
sea_99.format_score_year(r"D:\\MostCommonScore\\CSVs\\1999.csv")

# 2000's
sea_00 = ScoreFormat()
sea_00.format_score_year(r"D:\\MostCommonScore\\CSVs\\2000.csv")

sea_01 = ScoreFormat()
sea_01.format_score_year(r"D:\\MostCommonScore\\CSVs\\2001.csv")

sea_02 = ScoreFormat()
sea_02.format_score_year(r"D:\\MostCommonScore\\CSVs\\2002.csv")

sea_03 = ScoreFormat()
sea_03.format_score_year(r"D:\\MostCommonScore\\CSVs\\2003.csv")

sea_04 = ScoreFormat()
sea_04.format_score_year(r"D:\\MostCommonScore\\CSVs\\2004.csv")

sea_05 = ScoreFormat()
sea_05.format_score_year(r"D:\\MostCommonScore\\CSVs\\2005.csv")

sea_06 = ScoreFormat()
sea_06.format_score_year(r"D:\\MostCommonScore\\CSVs\\2006.csv")

sea_07 = ScoreFormat()
sea_07.format_score_year(r"D:\\MostCommonScore\\CSVs\\2007.csv")

sea_08 = ScoreFormat()
sea_08.format_score_year(r"D:\\MostCommonScore\\CSVs\\2008.csv")

sea_09 = ScoreFormat()
sea_09.format_score_year(r"D:\\MostCommonScore\\CSVs\\2009.csv")

# 2010's
sea_10 = ScoreFormat()
sea_10.format_score_year(r"D:\\MostCommonScore\\CSVs\\2010.csv")

sea_11 = ScoreFormat()
sea_11.format_score_year(r"D:\\MostCommonScore\\CSVs\\2011.csv")

sea_12 = ScoreFormat()
sea_12.format_score_year(r"D:\\MostCommonScore\\CSVs\\2012.csv")

sea_13 = ScoreFormat()
sea_13.format_score_year(r"D:\\MostCommonScore\\CSVs\\2013.csv")

sea_14 = ScoreFormat()
sea_14.format_score_year(r"D:\\MostCommonScore\\CSVs\\2014.csv")

sea_15 = ScoreFormat()
sea_15.format_score_year(r"D:\\MostCommonScore\\CSVs\\2015.csv")

sea_16 = ScoreFormat()
sea_16.format_score_year(r"D:\\MostCommonScore\\CSVs\\2016.csv")

sea_17 = ScoreFormat()
sea_17.format_score_year(r"D:\\MostCommonScore\\CSVs\\2017.csv")

sea_18 = ScoreFormat()
sea_18.format_score_year(r"D:\\MostCommonScore\\CSVs\\2018.csv")

sea_19 = ScoreFormat()
sea_19.format_score_year(r"D:\\MostCommonScore\\CSVs\\2019.csv")


# 2020's
sea_20 = ScoreFormat()
sea_20.format_score_year(r"D:\\MostCommonScore\\CSVs\\2020.csv")

sea_21 = ScoreFormat()
sea_21.format_score_year(r"D:\\MostCommonScore\\CSVs\\2021.csv")

sea_22 = ScoreFormat()
sea_22.format_score_year(r"D:\\MostCommonScore\\CSVs\\2022.csv")

allYearScores = ScoreFormat()
allYearScores.all_years()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



