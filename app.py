import streamlit as st

# Set the page configuration
st.set_page_config(page_title="My Homepage", layout="wide")

# Main navigation (Home and Machine Learning tabs in the sidebar)
with st.sidebar:
    st.header("Navigation")
    main_tab = st.selectbox("Choose a section", ["Home", "Machine Learning"])

# Home Tab Content
if main_tab == "Home":
    st.markdown('<h1 style="text-align: center; font-size:50px;">Yashwanth Reddy Thallapalli</h1>', unsafe_allow_html=True)
    
    # Columns for the About Me section
    col1, col2 = st.columns([1, 2])  # Image in col1, text in col2

    with col1:
        st.image("20240908_235437.jpg", caption="This is me!")  # Your profile image

    with col2:
        st.header("About Me")  # Header is now applied to the text side
        st.write("""
            A graduate student currently enrolled in the Masters in Data Science program at the University of Colorado Boulder.
            I hold an undergraduate degree in Bachelor of Technology in Electronics and Communication Engineering with 2+ years of work experience
            as a Senior Data Science Associate.
        """)


# Machine Learning Tab Content with Sub-Tabs
elif main_tab == "Machine Learning":
    # Display the title first, centered
    st.markdown('<h1 style="text-align: center;">Global Air Quality Analysis</h1>', unsafe_allow_html=True)
    
    # Display the image using st.image() without any additional HTML/CSS
    st.image("pexels-pixabay-221012.jpg", use_column_width=True)

    # Nested sub-tabs under Machine Learning, also in the sidebar
    with st.sidebar:
        sub_tab = st.selectbox("Choose a topic", ["Introduction", "Data Gathering", "Data Prep/EDA", "Conclusions"])

    if sub_tab == "Introduction":
        st.subheader("Introduction")
        st.write("""
            The topic of air quality has become increasingly relevant in today’s world. Rapid urbanization and industrialization have contributed significantly to the decline in air quality in many of the world's major cities. Pollutants such as PM2.5, PM10, CO, NO2, and O3 have had a severe impact on human health, contributing to respiratory diseases, cardiovascular issues, and premature deaths.

        """)

        st.write("""
            This project focuses on analyzing air quality across multiple cities globally, including London, Delhi, and Denver, from 2007 to 2024. By collecting data on key pollutants, we aim to explore the trends in air pollution over time, examine the geographical differences, and investigate the factors contributing to poor air quality. The cities selected for this analysis represent a wide range of geographical locations, economic development stages, and pollution levels, making this a comprehensive study of global air quality.

        """)

        st.subheader("Motivation")
        st.write("""
        The motivation behind this project is driven by the urgent need to better understand air pollution’s impact on urban environments. With millions of premature deaths attributed to air pollution globally, understanding the patterns and sources of pollution is critical to shaping policy responses and implementing mitigation strategies. This project seeks to contribute to this understanding by providing a detailed analysis of pollution data, uncovering insights into the main contributors, and identifying trends across different cities.
        """)

        st.subheader("Previous Works on Air Quality Prediction Using Machine Learning")
        st.write("""
        1. A comprehensive review by Méndez et al. (2023) examined 155 papers on machine learning models for air quality forecasting from 2011-2021. Key findings include:
            - Deep learning models were widely used, especially for predicting pollutant concentrations and air quality indices.
            - Common algorithms included artificial neural networks, decision trees, and support vector machines.
            - Ensemble models combining multiple techniques often outperformed individual models.

        2. Kumar et al. (2022) analyzed 6 years of air pollution data from 23 Indian cities. They:
            - Used correlation analysis for feature selection.
            - Applied 5 machine learning models to predict air quality index (AQI).
            - Found XGBoost performed best among the models tested.

        3. A systematic review by Bellinger et al. (2017) on data mining and machine learning for air pollution epidemiology found:
            - 18 studies using ML techniques for forecasting/prediction.
            - Most focused on predicting pollutant concentrations or AQI.
            - Some innovative data sources like social media were utilized.

        4. Gokulan et al. (2023) developed a deep learning framework to predict AQI in Indian cities, incorporating:
            - Long short-term memory (LSTM) networks.
            - Feature selection using metaheuristic algorithms.
            - Analysis of COVID-19 lockdown impacts on air quality.

        5. Gupta et al. (2023) conducted a comparative analysis of machine learning techniques for AQI prediction, using:
            - Support vector regression (SVR) as a widely-used method.
            - Multiple algorithms to quantify pollutant levels and predict AQI.

        These studies demonstrate the wide application of machine learning for air quality prediction globally, with a variety of algorithms and approaches being explored. The research highlights the potential of ML techniques to improve air quality forecasting and analysis.
        """)

        st.subheader("Questions This Analysis Hopes to Answer")

        st.write("""
        1. What is the trend of air pollution across different seasons in major cities?
        2. Are there specific pollutants that are consistently higher in one city compared to others?
        3. How do meteorological factors such as humidity or wind speed influence air quality levels?
        4. Is there a correlation between population density and higher pollutant levels?

        5. Which cities have the most significant air quality improvements or declines from 2023 to 2024?
        6. How do policies implemented in cities such as London or Delhi affect air quality improvements?
        7. What are the key health impacts linked to air pollution levels in cities with high PM2.5 and PM10?
        8. Is there a correlation between traffic congestion and spikes in NO2 and CO levels in urban areas?
        9. Can machine learning models predict future pollution levels based on past trends?
        10. How do air quality trends differ between highly industrialized and less industrialized cities?
        """)

    elif sub_tab == "Data Gathering":
        st.subheader("Data Gathering")

        st.write("""
        The air quality dataset used in this project was collected from two primary sources:

        1. **OpenAQ API**

        The OpenAQ API was utilized to gather real-time and historical air quality data for the city of London. The data spans from January 2023 to August 2024, and includes key pollutants such as PM2.5, PM10, CO, SO2, NO2, and O3. This API provides a comprehensive dataset with pollutant levels measured at different times of the day.

        *Source*: [OpenAQ API](https://explore.openaq.org)

        The key parameters used to fetch the data included:
        - **City**: London
        - **Pollutants**: PM2.5, PM10, CO, SO2, NO2, O3, NO, BC
        - **Date Range**: January 2023 to August 2024

        This dataset provided a crucial real-time component to the analysis by offering recent air quality data for London.
        """)

        st.image("2.png", use_column_width=True, caption="Data retrieved from OpenAQ API")
                 
        st.write("""
        2. **Google BigQuery - OpenAQ Public Dataset**

        In addition to the API, historical air quality data was retrieved from the OpenAQ Public Dataset hosted on Google BigQuery. This dataset contains global air quality measurements from **2007 to 2022** across multiple cities. It includes measurements for several pollutants and allows for comprehensive time-series analysis of air quality across different regions.

        *Source*: [OpenAQ Public Dataset - BigQuery](https://console.cloud.google.com/marketplace/product/openaq/real-time-air-quality)

        The BigQuery dataset covers numerous cities worldwide, enabling a broad analysis of air quality patterns from 2007 to 2022. This large dataset allowed for comparisons across multiple years and cities to explore trends in air pollution over time.

        Together, these two datasets contributed over **6 million data points** for the project, creating a rich resource for analysis.

        In total, the data collected from both the OpenAQ API and BigQuery covers a wide range of geographical locations and time periods, providing a robust basis for air quality analysis from 2007 to 2024.
        """)
        
        st.image("1.png", use_column_width=True, caption="Data retrieved from Google BigQuery")

    elif sub_tab == "Data Prep/EDA":
        st.subheader("Data Prep/EDA")
        st.subheader("Combining API and BigQuery Datasets")

        st.write("""
        The air quality data used for this analysis was collected from two main sources: the OpenAQ API and Google BigQuery. Several steps were taken to clean and prepare the data for analysis.
        """)

        # Step 1: Handling missing city values
        st.write("""
        ##### Step 1: Handling Missing City Values

        - OpenAQ API data had missing city values, filled in with 'London' for missing entries.
        """)

        # Step 2: Extracting Latitude and Longitude from Coordinates
        st.write("""
        ##### Step 2: Extracting Latitude and Longitude from Coordinates

        - Extracted 'latitude' and 'longitude' from the 'coordinates' column.
        - Created a new 'location_geom' column combining the extracted latitude and longitude.
        - Dropped the original 'coordinates' column after extraction.
        """)

        # Step 3: Renaming API Columns to Match BigQuery
        st.write("""
        ##### Step 3: Renaming API Columns to Match BigQuery

        - Renamed API dataset columns to match BigQuery column names for consistency (e.g., 'parameter' to 'pollutant', 'date' to 'timestamp').
        """)

        # Step 4: Formatting Timestamp and Cleaning Source Name
        st.write("""
        ##### Step 4: Formatting Timestamp and Cleaning Source Name

        - Reformatted the 'timestamp' column to ensure proper time zone formatting.
        - Converted 'source_name' column to numeric values where possible, setting invalid entries as NaN.
        """)

        # Step 5: Combining the Datasets
        st.write("""
        ##### Step 5: Combining the Datasets

        - Combined both the cleaned datasets from BigQuery (df1) and API (df2) into one dataset.
        - Saved the combined dataset for further analysis as 'combined_air_quality_data.csv'.
        """)

        # Combined Dataset Image (Screenshot)
        st.image("3.png", use_column_width=True, caption="Combined Dataset")
        
        st.subheader("Data Cleaning")

        st.write("""
        The dataset collected from both the OpenAQ API and Google BigQuery required thorough cleaning to ensure consistency and accuracy. The following steps outline the cleaning process applied to the dataset:
        """)

        # Step 1: Handling Missing Values
        st.write("""
        ### Step 1: Handling Missing Values

        - The `location`, `city`, `averaged_over_in_hours`, and `source_name` columns contained missing values.
        - The `longitude` column had one missing value, which was dropped to ensure no invalid geographical data remained in the dataset.
        - DEFRA was identified as the main source for a large number of data points in the London dataset.
        - Missing values in the `source_name` column were filled with 'DEFRA' instead of being dropped to preserve data integrity.         
        """)
        st.write("""
                 """)
        st.write("""
        - There are 10,809 unique locations in the dataset.
        - The top 30 locations with the highest number of data points were selected for visualization.
        - A bar plot was created to show these top 30 locations, with the number of data points on the y-axis.
        """)
        st.image("4.png", use_column_width=True, caption="Top 30 Locations by Number of Data Points")

        st.write("""
        - The 'averaged_over_in_hours' column had missing values, which were removed before visualizing.
        - After cleaning, a histogram was plotted to show the distribution of 'averaged_over_in_hours'.
        - The plot provides insight into how often data was averaged over specific periods.
        """)
        st.image("5.png", use_column_width=True, caption="Distribution of Averaged Over in Hours")

        st.write("""
        Upon reviewing the column `averaged_over_in_hours`, it was found that the data contained a strange distribution, including negative values. Since these values do not make logical sense in the context of averaging hours, the decision was made to drop the column entirely.
        """)        

        # Reverse Geocoding Section
        st.subheader("Handling Missing Cities Using Reverse Geocoding")

        st.write("""
        During the data preparation phase, it was identified that several rows in the dataset were missing city and location names. To fill these missing values, the latitude and longitude information present in the dataset was used to perform reverse geocoding.
        """)

        st.write("""
        ### Reverse Geocoding with OpenCage API

        For each missing city and location, the corresponding latitude and longitude pair was reverse-geocoded using the OpenCage Geocoding API. This allowed for retrieving city and road names based on the provided coordinates. 

        - **API Source**: The OpenCage API
        - **Source Link**: [OpenCage Geocoding API](https://opencagedata.com)
        - **API Key**: The API key was used to authenticate requests.
        - **Handling Geocoded Data**: Once the reverse geocoding process was completed, the new city and location values were merged back into the dataset. Rows that had previously missing values were updated accordingly.
        
        A total of 548 missing city names were successfully updated using reverse geocoding. The geocoded data was merged back into the main dataset, ensuring completeness and accuracy of geographical data.
        """)

        # Data Cleaning: Handling Missing City and Location Values
        st.subheader("Handling Missing City and Location Values")

        st.image("6.png", use_column_width=True, caption="Top 10 Cities by Overall Percentage (Including NaNs)")

        st.write("""
        After visualizing the top 10 cities, it was found that approximately 1.22% of the data had missing values for the city field (shown as NaN). Since this represents a very small portion of the data (only 1.22%), it was decided to remove these rows to ensure data consistency without losing significant information.
        """)

        st.write("""
        Additionally, 756 rows were found to have missing 'location' values. Since this is a very small fraction of the overall dataset, these rows were also removed to maintain data accuracy.
        """)

        st.write("""
        In the dataset, air quality data comes from multiple countries. To better understand the distribution of data among these countries, a pie chart was created to show the proportion of data points contributed by each country.

        Countries contributing less than 1.5% of the total data were grouped into an "Others" category for simplification.
        """)

        # Displaying the Pie Chart of Country Proportion
        st.image("7.png", use_column_width=True, caption="Countries by Air Quality Data Proportion (with Others)")

        # Data Cleaning: Outlier Removal and Capping of Pollutant Values
        st.subheader("Data Cleaning: Outlier Removal and Capping of Pollutant Values")

        st.image("8.png", use_column_width=True, caption="Box Plot of Pollutant Values (Before Cleaning)")

        st.write("""
        In the dataset, there were several cases of negative values for pollutants, as well as extreme outliers. A multi-step cleaning process was applied to handle these issues:

        ##### Step 1: Remove Negative Pollutant Values
        Negative values were identified in the pollutant data, which are logically incorrect. These rows were removed from the dataset to maintain data integrity.

        ##### Step 2: Cap Extremely High Values
        Extremely high pollutant values that exceed globally recorded maximum levels were capped based on real-world limits for each pollutant. This ensures the data stays within a realistic range.

        - Approximate max recorded pollutant values used for capping:
        - **PM2.5**: 1000 µg/m³
        - **PM10**: 2000 µg/m³
        - **O3**: 500 µg/m³
        - **NO2**: 1000 µg/m³
        - **CO**: 30000 µg/m³
        - **SO2**: 1000 µg/m³
        - **BC**: 100 µg/m³
        - **NO**: 500 µg/m³

        ##### Step 3: Apply IQR Method to Remove Remaining Outliers
        The Interquartile Range (IQR) method was used to remove remaining outliers. Values outside 1.5 times the IQR from the first and third quartiles were removed for each pollutant to ensure cleaner data distribution.

        ##### Step 4: Visualize the Cleaned Data
        After applying these cleaning steps, the pollutant values were visualized using a box plot to confirm that the data was cleaned properly.
        """)

        # Displaying Boxplot for Pollutant Values
        st.image("9.png", use_column_width=True, caption="Box Plot of Pollutant Values (After Cleaning)")

        # Data Cleaning: Chinese Locations and Misclassified Rows
        st.subheader("Handling Chinese Locations and Misclassified Rows")

        st.write("""
        During the data cleaning process, several locations and cities in the dataset were found to contain Chinese characters. These entries needed to be translated into English for consistency, and many of them appeared to have been misclassified with coordinates pointing to locations in Africa or other incorrect regions. The steps taken to handle this are as follows:

        ##### Step 1: Identify Locations with Chinese Characters
        The dataset was scanned for rows where the city or location names contained Chinese characters. This helped identify potential errors or misclassified locations that needed correction.

        ##### Step 2: Visualizing Chinese Locations
        We visualized locations in China and Taiwan to understand the distribution of these points and see if there were any obvious anomalies. The scatter plot highlighted regions that might have incorrect data.

        ##### Step 3: Handling Misclassified Rows
        A significant number of rows were identified where the latitudes and longitudes corresponded to locations in Africa, despite being labeled as locations in China. These rows were considered misclassified.

        - **Misclassified rows**: Rows outside the valid range for China and Taiwan were flagged for further inspection.
        - **Correcting misclassified locations**: The OpenCage API was used to attempt reverse geocoding to fix these misclassified entries. Unfortunately, in many cases, it wasn’t possible to retrieve valid city and location names using the API.
        - **Drop misclassified rows**: Since the OpenCage API couldn’t provide valid location data for these rows, they were ultimately dropped from the dataset.
        """)

        # Visualizations (Example Visualization Placeholder)
        st.image("10.png", use_column_width=True, caption="Scatter Plot of Locations with Chinese Characters")

        # Final Note
        st.write("""
        By cleaning the misclassified and Chinese-character rows, we ensured that the data was more accurate and consistent for the analysis. This step was critical, as these incorrect entries could have skewed the analysis and impacted the insights derived from the data.
        """)

        # Data Visualization: Geographical Distribution of Air Quality Data
        st.subheader("Geographical Distribution of Air Quality Data")

        st.write("""
        To better understand the geographical distribution of air quality data across the world, we visualized a scatter plot where each point represents a location where air quality data was recorded. The color of the points corresponds to the pollutant type, and the size of the points represents the pollutant's recorded value.

        Given the large size of the dataset, a random sample (0.1%) of the data was used for the visualization to keep the rendering efficient while still providing meaningful insights.
        """)
        st.image("11.png", use_column_width=True, caption="Geographical Distribution of Air Quality Data, showing pollutant types across different regions.")

        st.subheader("Correlation Between Pollutants")
        st.image("12.png", use_column_width=True, caption="Correlation Heatmap of Pollutants")
        st.write("""
        The correlation heatmap shown below displays how various pollutants, such as PM10, NO2, CO, and others, correlate with each other based on the average pollutant values. 
        For example, pollutants PM10 and PM25 have a strong positive correlation (0.85), while O3 and CO show almost zero correlation. 
        This analysis helps understand how changes in one pollutant may influence or predict changes in another.
        """)

        st.subheader("Treemap of Average NO2 Levels by Country")

        st.write("""
        The treemap below visualizes the average NO2 levels across different countries. Each country is represented by a block, 
        and the size and color intensity indicate the level of NO2 in that country. Countries with higher levels of NO2 appear in 
        brighter and larger blocks, making it easier to compare pollution levels across regions.

        NO2 is a significant air pollutant primarily produced from burning fossil fuels. It affects air quality and poses health 
        risks, contributing to respiratory issues and environmental challenges like acid rain.
        """)

        st.image("13.png", use_column_width=True, caption="Treemap of Average NO2 Levels by Country")

        st.subheader("Top Countries by Average Pollutant Values")

        st.write("""
        The charts below show the top countries for each pollutant based on average values. 
        For each pollutant, the top 3 countries (or all countries if fewer than 3) are displayed to highlight regions 
        with significant pollutant levels.
        """)

        st.image("14.png", use_column_width=True, caption="Top Countries by Average Pollutant Values")

        st.write("""
        During the analysis, it was found that the pollutant value 'no' only occurred once in the dataset. Given its insignificance, 
        we removed this row to maintain data integrity.
        """)

        st.write("""
        During the data cleaning process, the `location_geom` column was identified as redundant. This column stored geographical 
        points in the format 'POINT(lat lon)', which is essentially duplicating the information already available in the `latitude` 
        and `longitude` columns. As the `latitude` and `longitude` columns are more straightforward to work with, the `location_geom` 
        column was dropped to reduce redundancy and simplify the dataset.
        """)

        st.subheader("Final Cleaned Dataset")

        st.write("""
        The final cleaned dataset is the result of thorough data preparation and cleaning steps applied to the raw air quality data. 
        The following key cleaning operations were performed:

        - **Handling Missing Values**: Missing values in key columns like `city` and `location` were handled using reverse geocoding 
        and imputation techniques. Rows with missing or incorrect data were either updated or removed.
        
        - **Outliers Removal**: Outliers in pollutant values were identified and handled using methods like capping extreme values 
        based on known global pollutant limits and applying the IQR method to remove further anomalies.

        - **Pollutant Data Correction**: Rows with negative or highly improbable pollutant values were cleaned, with extreme values 
        being capped at their realistic maxima based on known environmental data.

        - **Geographical Misclassifications**: Rows containing misclassified geographical information were cleaned using API-based 
        reverse geocoding, and rows with irreparable data were removed.

        - **Column Redundancy**: Redundant columns such as `location_geom` that duplicated information already provided by `latitude` 
        and `longitude` were dropped.

        The resulting dataset contains clean, structured, and ready-to-analyze air quality data from a variety of global locations, 
        enabling a clearer exploration of pollution levels, sources, and geographic distribution.
        """)

        st.write("Uncleaned Dataset:")
        st.image("3.png", use_column_width=True, caption="Uncleaned Dataset")

        # Add a placeholder to display the dataset once it's uploaded or ready
        st.write("Cleaned Dataset:")

        st.image("15.png", use_column_width=True, caption="Cleaned Dataset")

    elif sub_tab == "Conclusions":
        st.subheader("Conclusions")
        st.write("This section concludes the Machine Learning topics discussed.")

# Social Links Section (LinkedIn and GitHub)
st.write("### Connect with me:")
col1, col2 = st.columns(2)

with col1:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/yashwanth-reddy-thallapalli-1117701b3/)")

with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-View%20Profile-black)](https://github.com/starlord-31)")

# Footer
st.markdown("---")
st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/ML_Project.ipynb)", unsafe_allow_html=True)
st.write("© 2024 Yashwanth Reddy Thallapalli")
