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
        st.image("Images/20240908_235437.jpg", caption="This is me!")  # Your profile image

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
    st.image("Images/pexels-pixabay-221012.jpg", use_column_width=True)

    # Nested sub-tabs under Machine Learning, also in the sidebar
    with st.sidebar:
        sub_tab = st.selectbox("Choose a topic", ["Introduction", "Data Gathering", "Data Prep/EDA", "PCA", "Clustering", "Association Rule Mining", "Conclusions"])

    if sub_tab == "Introduction":
        st.subheader("Introduction")
        st.write("""
            Air quality has become one of the most critical environmental concerns in the modern era, as rapid urbanization and industrialization continue to degrade the atmosphere. Poor air quality has been linked to a wide range of health problems, including respiratory diseases, cardiovascular conditions, and even premature death. This is particularly true for cities with high population densities and significant industrial activity. Pollutants such as particulate matter (PM2.5, PM10), carbon monoxide (CO), nitrogen dioxide (NO2), and ozone (O3) are among the most harmful to human health. Exposure to these pollutants is not only a public health concern but also has significant economic implications, as it leads to increased healthcare costs and reduced worker productivity. In this project, air quality data from various cities around the world are analyzed to identify trends, key pollutants, and factors contributing to pollution levels.

        """)

        st.write("""
            This project focuses on analyzing air quality across multiple cities globally, including major urban centers like London, Delhi, and Denver. These cities were selected for their geographical diversity, economic status, and varying levels of air pollution. By gathering data on major air pollutants between 2007 and 2024, the aim is to explore the temporal and spatial variations in pollution levels. For instance, while cities like London may experience pollution spikes due to traffic emissions, industrial centers like Delhi are more likely to be impacted by coal burning and vehicular exhaust. The analysis will look at pollutants such as PM2.5 and PM10, which are small enough to penetrate deep into the lungs, as well as gases like CO, NO2, and O3, which have known harmful effects on human health. Understanding these differences is crucial for formulating effective policy interventions aimed at reducing pollution levels.

        """)

        st.write("""
            In addition to simply analyzing air quality data, this project also applies advanced machine learning techniques such as Principal Component Analysis (PCA) and various clustering algorithms. PCA will help in reducing the dimensionality of the dataset, allowing for easier interpretation of the underlying factors contributing to air quality variations. Clustering techniques such as KMeans, hierarchical clustering, and DBSCAN will be used to identify natural groupings within the data. These methods will allow for a more detailed analysis of how pollution levels are influenced by geographical factors, economic activity, and seasonal changes. Furthermore, this analysis will offer insights into the relationships between different pollutants, helping to pinpoint which combinations of pollutants are most harmful in specific urban environments. By leveraging these machine learning techniques, the project aims to provide a comprehensive understanding of global air quality trends and contribute to efforts in reducing pollution and improving public health.

        """)


        st.subheader("Motivation")
        st.write("""
        The motivation behind this project is driven by the urgent need to better understand air pollution’s impact on urban environments. With millions of premature deaths attributed to air pollution globally, understanding the patterns and sources of pollution is critical to shaping policy responses and implementing mitigation strategies. This project seeks to contribute to this understanding by providing a detailed analysis of pollution data, uncovering insights into the main contributors, and identifying trends across different cities.
        """)

        st.subheader("Previous Works on Air Quality Prediction Using Machine Learning")
        st.write("""
        1. [A comprehensive review by Méndez et al. (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9933038/) examined 155 papers on machine learning models for air quality forecasting from 2011-2021. Key findings include:
            - Deep learning models were widely used, especially for predicting pollutant concentrations and air quality indices.
            - Common algorithms included artificial neural networks, decision trees, and support vector machines.
            - Ensemble models combining multiple techniques often outperformed individual models.

        2. [Kumar et al. (2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9107909/) analyzed 6 years of air pollution data from 23 Indian cities. They:
            - Used correlation analysis for feature selection.
            - Applied 5 machine learning models to predict air quality index (AQI).
            - Found XGBoost performed best among the models tested.

        3. [A systematic review by Bellinger et al. (2017)](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-017-4914-3) on data mining and machine learning for air pollution epidemiology found:
            - 18 studies using ML techniques for forecasting/prediction.
            - Most focused on predicting pollutant concentrations or AQI.
            - Some innovative data sources like social media were utilized.

        4. [Gupta et al. (2023)](https://onlinelibrary.wiley.com/doi/10.1155/2023/4916267) conducted a comparative analysis of machine learning techniques for AQI prediction, using:
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

        5. Which cities have the most significant air quality improvements or declines from 2007 to 2022?
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

        The OpenAQ API was utilized to gather real-time and historical air quality data for the city of London. The data spans from January 2023 to August 2024, and includes key pollutants such as PM2.5, PM10, CO, SO2, NO2, BC, and O3. This API provides a comprehensive dataset with pollutant levels measured at different times of the day.

        *Source*: [OpenAQ API](https://explore.openaq.org)

        The key parameters used to fetch the data included:
        - **City**: London
        - **Pollutants**: PM2.5, PM10, CO, SO2, NO2, O3, NO, BC
        - **Date Range**: January 2023 to August 2024

        This dataset provided a crucial real-time component to the analysis by offering recent air quality data for London.
        """)

        st.image("Images/2.png", use_column_width=True, caption="Data retrieved from OpenAQ API")
                 
        st.write("""
        2. **Google BigQuery - OpenAQ Public Dataset**

        In addition to the API, historical air quality data was retrieved from the OpenAQ Public Dataset hosted on Google BigQuery. This dataset contains global air quality measurements from **2007 to 2022** across multiple cities. It includes measurements for several pollutants and allows for comprehensive time-series analysis of air quality across different regions.

        *Source*: [OpenAQ Public Dataset - BigQuery](https://console.cloud.google.com/marketplace/product/openaq/real-time-air-quality)

        The BigQuery dataset covers numerous cities worldwide, enabling a broad analysis of air quality patterns from 2007 to 2022. This large dataset allowed for comparisons across multiple years and cities to explore trends in air pollution over time.

        Together, these two datasets contributed over **6 million data points** for the project, creating a rich resource for analysis.

        In total, the data collected from both the OpenAQ API and BigQuery covers a wide range of geographical locations and time periods, providing a robust basis for air quality analysis from 2007 to 2024.
        """)
        
        st.image("Images/1.png", use_column_width=True, caption="Data retrieved from Google BigQuery")
        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Introduction_Code.ipynb)", unsafe_allow_html=True)
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)", unsafe_allow_html=True)

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
        st.image("Images/3.png", use_column_width=True, caption="Combined Dataset")
        
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
        st.image("Images/4.png", use_column_width=True, caption="Top 30 Locations by Number of Data Points")

        st.write("""
        - The 'averaged_over_in_hours' column had missing values, which were removed before visualizing.
        - After cleaning, a histogram was plotted to show the distribution of 'averaged_over_in_hours'.
        - The plot provides insight into how often data was averaged over specific periods.
        """)
        st.image("Images/5.png", use_column_width=True, caption="Distribution of Averaged Over in Hours")

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

        st.image("Images/6.png", use_column_width=True, caption="Top 10 Cities by Overall Percentage (Including NaNs)")

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
        st.image("Images/7.png", use_column_width=True, caption="Countries by Air Quality Data Proportion (with Others)")

        # Data Cleaning: Outlier Removal and Capping of Pollutant Values
        st.subheader("Data Cleaning: Outlier Removal and Capping of Pollutant Values")

        st.image("Images/8.png", use_column_width=True, caption="Box Plot of Pollutant Values (Before Cleaning)")

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
        st.image("Images/9.png", use_column_width=True, caption="Box Plot of Pollutant Values (After Cleaning)")

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
        st.image("Images/10.png", use_column_width=True, caption="Scatter Plot of Locations with Chinese Characters")

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
        st.image("Images/11.png", use_column_width=True, caption="Geographical Distribution of Air Quality Data, showing pollutant types across different regions.")

        st.subheader("Correlation Between Pollutants")
        st.image("Images/12.png", use_column_width=True, caption="Correlation Heatmap of Pollutants")
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

        st.image("Images/13.png", use_column_width=True, caption="Treemap of Average NO2 Levels by Country")

        st.subheader("Top Countries by Average Pollutant Values")

        st.write("""
        The charts below show the top countries for each pollutant based on average values. 
        For each pollutant, the top 3 countries (or all countries if fewer than 3) are displayed to highlight regions 
        with significant pollutant levels.
        """)

        st.image("Images/14.png", use_column_width=True, caption="Top Countries by Average Pollutant Values")

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
        st.image("Images/3.png", use_column_width=True, caption="Uncleaned Dataset")

        # Add a placeholder to display the dataset once it's uploaded or ready
        st.write("Cleaned Dataset:")


        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Introduction_Code.ipynb)", unsafe_allow_html=True)
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)", unsafe_allow_html=True)

    elif sub_tab == "PCA":
        st.subheader("PCA")
        st.markdown("#### Overview")
        st.write("Principal Component Analysis (PCA) is a statistical technique that simplifies a dataset by reducing its dimensionality, while still retaining as much of the data’s variance as possible. This reduction is achieved by transforming the data into new, uncorrelated variables called principal components. The first principal component is the direction in which the data varies the most, the second component captures the next highest variance, and so on. Each successive principal component is orthogonal (uncorrelated) to the previous ones.")
        st.write("PCA works by finding the axes (principal components) that capture the most variance in the data. This process involves creating a covariance matrix, calculating the eigenvalues and eigenvectors, and projecting the original data onto these new axes. The resulting components are ranked by the amount of variance they explain. Typically, the first few components capture most of the variation, allowing for effective dimensionality reduction.")
        
        st.markdown("##### The two images below illustrate the concept of PCA:")
        st.image("Images/PCA1.png", use_column_width=True, caption="PCA Transformation of Data")
        st.write("The above image shows a 2D dataset before and after PCA transformation. The original data is represented in terms of the x and y axes, and PCA transforms this into new axes (principal components) that maximize the variance in the data.")
        
        st.write("""
                 """)

        st.image("Images/PCA2.png", use_column_width=True, caption="Variance Explained by Principal Components")
        st.write("The above image depicts the variance explained by each principal component. The eigenvalues are proportional to the variance captured by each component, and the first few components typically capture the majority of the variance. This graph helps in selecting how many components to keep, as it shows how much of the original data’s variance is retained when reducing dimensionality.")

        st.write("In this project, PCA is applied to reduce the dimensionality of the air quality dataset, which contains multiple pollutants such as PM2.5, PM10, NO2, SO2, CO, and O3. By using PCA, the data can be transformed into a smaller number of principal components while still capturing the majority of the variance present in the original dataset. This reduction in dimensionality simplifies the analysis process, making it easier to visualize and interpret patterns in the data. For example, by reducing the data to 2 or 3 principal components, approximately 54-69% of the total variance is retained, allowing for efficient downstream tasks such as clustering and association rule mining while preserving the most significant information about pollutant variability across cities.")

        st.markdown("#### Data Prep and Code")
        st.write("""

        1. The `final_cleaned.csv` dataset is loaded, which contains air quality data (pollutant levels) and geographic information (latitude and longitude).
        
        2. The pollutants (`PM2.5`, `PM10`, `NO2`, `SO2`, `O3`, `CO`) are separated into columns with each location's specific data being indexed by `latitude` and `longitude`. This restructuring allows each pollutant to be analyzed individually.

        3. Rows with missing values are dropped, ensuring only complete data is used for further analysis. This step is critical to avoid issues during normalization and clustering.

        4. The data is normalized using `StandardScaler` so that all features (pollutant values, latitude, longitude) are transformed to have a mean of 0 and a standard deviation of 1. Normalization ensures that no single feature dominates the others during analysis, making the data suitable for PCA and clustering.

        """)
        st.image("Images/15.png", use_column_width=True, caption="Dataset Before Prep")
        st.image("Images/PCA3.png", use_column_width=True, caption="Dataset after Prep")

        st.image("Images/Cluster7.png", use_column_width=True, caption="PCA-Transformed Data")


        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/PCA.ipynb)", unsafe_allow_html=True)
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)", unsafe_allow_html=True)

        st.markdown("#### Results")
        st.markdown("##### PCA with 2 components")
        st.write("""

        - **Principal Component Analysis (PCA)** was applied to reduce the dimensions of the dataset to 2 components. This reduction allows for better visualization while still retaining significant variance from the original data.

        - The scatter plot above represents the data transformed into 2 principal components. Each point corresponds to a sample from the dataset, projected onto the two most important components (PC1 and PC2). This enables a clearer understanding of patterns or clusters in the data.

        - The grid provides a clearer understanding of how the data is distributed across the principal components, and the axes are labeled accordingly to indicate the components being plotted.
        """)
        st.image("Images/PCA4.png", use_column_width=True, caption="PCA with 2 Components (2D)")

        st.markdown("##### PCA with 3 components")
        st.write("""

        - PCA was performed to reduce the dimensionality of the data to three principal components. This is useful for analyzing the data in a simplified 3D space while retaining as much variability from the original dataset as possible.

        - The 3D scatter plot visualizes the transformed dataset in the new three-dimensional space, where each axis represents one of the principal components (PC1, PC2, and PC3). The resulting plot shows how the data points are distributed across these three principal axes, with the majority of the data points concentrated in certain areas of the plot.

        - By using PCA in this way, it becomes easier to visualize and interpret complex datasets with many variables by projecting them into a lower-dimensional space without losing significant information.
        """)
        st.image("Images/PCA5.png", use_column_width=True, caption="PCA with 3 Components (2D)")
        st.write("""
                 """)
        st.write("After reducing the dataset to 2 dimensions, **54%** of the total variance is retained, meaning over half of the original information is preserved.")
        st.image("Images/PCA6.png", caption="Variance Explained by the First Two Components", use_column_width=True)
        st.write("""
                 """)
        st.write("After reducing the dataset to 3 dimensions, **69%** of the total variance is retained, preserving a significant portion of the original information.")
        st.image("Images/PCA7.png", caption="Variance Explained by the First Three Components", use_column_width=True)
        st.write("""
                 """)
        st.write("""
        PCA aims to reduce the dimensionality of the dataset while retaining the majority of the information (variance) present in the original data. 
        By calculating the cumulative explained variance, it becomes possible to determine how many principal components are needed to capture a certain percentage of the variance. 
        In this case, the goal was to retain at least **95%** of the variance in the data. 
        Upon running PCA on the normalized dataset, it was found that **7 components** are required to retain **95%** of the data's variance. 
        This helps reduce complexity while preserving essential information in the dataset. The result shows that using fewer dimensions can still capture the majority of the underlying structure in the data.
        """)
        st.image("Images/PCA8.png", caption="Number of Components to Retain 95% of Variance", use_column_width=True)
        st.image("Images/PCA10.png", caption="Cumulative Variance Explained by Principal Components", use_column_width=True)
        st.write("""
                 """)
        st.write("""
        Eigenvalues are proportional to the explained variance of the dataset. They represent the amount of variance captured by each principal component. The larger the eigenvalue, the more significant that principal component is in explaining the variance in the data.
        """)
        st.image("Images/PCA9.png", caption="Top Three Eigenvalues", use_column_width=True)

        st.write("""
        #### Conclusion

        Principal Component Analysis (PCA) was effectively applied to reduce the dimensionality of the dataset while retaining a significant amount of variance. This dimensionality reduction simplifies the data, making it easier to process, visualize, and analyze while still preserving the essential patterns present in the original high-dimensional dataset.

        The most important principal components identified by PCA captured the majority of the dataset’s variance, emphasizing their importance in explaining the key patterns in the data. By reducing the complexity of the dataset, PCA facilitates a more efficient analysis without significant loss of information. This dimensionality reduction method has proven valuable in enhancing the interpretability of the dataset, improving the overall analytical process by focusing on the most informative components.

        In conclusion, PCA successfully streamlined the data, retaining its critical information while simplifying its structure. This approach provides clearer insights, allows for improved visualization, and lays the foundation for further clustering or predictive analysis.
        """)

    elif sub_tab == "Clustering":
        st.subheader("Clustering")
        # Overview of Clustering
        st.write("""
        #### Clustering Tab - Overview

        Clustering is a widely used method in data analysis to group similar data points based on certain distance measures. In this project, clustering techniques are applied to group cities and pollutants based on their air quality similarities. This helps identify patterns that might not be evident when analyzing individual cities. The clustering techniques used include **KMeans (partition clustering)**, **hierarchical clustering**, and **DBSCAN (density-based clustering)**. Distance metrics play a key role in determining which data points belong to the same cluster, so they are essential in all these methods.
        """)

        # Explanation of Distance Metrics
        st.write("""
        #### Distance Metrics in Clustering
        In all clustering methods, distance measures are used to calculate how close or far data points are from each other. These metrics are crucial for determining cluster assignments. The following distance measures are commonly used:

        - **Euclidean Distance**: The straight-line distance between two points in Euclidean space. It is widely used in KMeans clustering.
        - **Manhattan Distance**: Measures the distance between two points along the axes at right angles (like navigating city blocks).
        - **Cosine Similarity**: Measures the cosine of the angle between two vectors, commonly used in text and document clustering.

        For this project, **Euclidean distance** is primarily used for partition and hierarchical clustering as it effectively measures similarities in pollution levels across different cities.
        """)

        # Add image for Distance Metrics
        st.image('Images/Cluster1.png', caption='Visual Representation of Distance Metrics')

        # Explanation of Partition Clustering (KMeans)
        st.write("""
        #### Partition Clustering (KMeans)
        KMeans is a partition-based clustering algorithm that divides data into *k* clusters by iteratively minimizing the variance within each cluster. It assigns each data point to the nearest cluster centroid using **Euclidean distance**, and recalculates centroids based on the current cluster assignments until convergence is achieved.

        - **Advantages**: KMeans is simple, fast, and efficient, especially for large datasets where clusters are well-separated. It scales well and is easy to implement. 
        - **Drawbacks**: The algorithm is sensitive to the initial choice of centroids, which can lead to different results. It also requires specifying the number of clusters (*k*) beforehand, which may not always be known.

        In this project, **KMeans** is used to identify clusters of cities with similar air pollution profiles. Through the Silhouette method, the optimal number of clusters is determined, and cities are grouped accordingly.
        """)

        # Image 1 Placeholder for KMeans Visualization
        st.image('Images/Cluster2.png', caption='KMeans Clustering Visualization')

        # Explanation of Hierarchical Clustering
        st.write("""
        #### Hierarchical Clustering
        Hierarchical clustering builds a hierarchy of clusters using **distance measures** (usually Euclidean or Manhattan) to calculate how closely data points are related. In agglomerative clustering, each data point starts as its own cluster, and pairs of clusters are merged iteratively based on their proximity until all points belong to a single cluster.

        - **Advantages**: No need to specify the number of clusters upfront, and it provides a comprehensive view of the data at different levels of granularity through a dendrogram.
        - **Drawbacks**: It is computationally intensive for large datasets and sensitive to noise and outliers. Hierarchical clustering is harder to scale due to its quadratic complexity.

        In the project, **hierarchical clustering** helps reveal hierarchical relationships between cities based on air quality levels. The dendrogram created shows how similar or different cities are in terms of pollution.
        """)

        # Image 2 Placeholder for Hierarchical Clustering Visualization
        st.image('Images/Cluster3.png', caption='Hierarchical Clustering Dendrogram')
        
        # Explanation of DBSCAN
        st.write("""
        #### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
        DBSCAN is a density-based clustering method that identifies clusters based on regions of high data density. Instead of relying on distance metrics like Euclidean distance for all points, DBSCAN looks for dense clusters and labels points in sparse regions as outliers.

        - **Advantages**: DBSCAN can find clusters of arbitrary shapes and sizes, and it does not require specifying the number of clusters beforehand. It works well for datasets with noise and varying densities.
        - **Drawbacks**: The performance of DBSCAN is sensitive to the choice of hyperparameters (*eps* and *min_samples*). It may struggle with varying densities within the same dataset.

        In this project, **DBSCAN** is useful for detecting outliers and unusual pollution patterns in specific cities that do not fit well into larger clusters.
        """)

        # Add image for DBSCAN Clustering
        st.image('Images/Clustering4.png', caption='DBSCAN Clustering Visualization')

        st.markdown("#### Data Preperation")

        st.image("Images/15.png", use_column_width=True, caption="Dataset Before Preperation")
        st.write("""
                 """)
        st.write("""
        1. The columns `latitude` and `longitude` are separated from the main dataset for later use in merging back geographical data.
        2. The data is pivoted to create individual columns for each pollutant, such as `pm25`, `pm10`, `no2`, `so2`, `o3`, and `co`. This makes it easier to analyze the pollutant levels for each location and timestamp.
        3. The latitude and longitude columns are merged back with the pivoted data to retain geographical information alongside the pollutant data.
        4. Rows with any missing pollutant values are removed to ensure clean data is used for further processing and analysis.
        5. Below is the first five rows of the raw pollutant data before normalization.

        """)
        st.image("Images/Cluster5.png", use_column_width=True, caption="Dataset Before Normalization")
        st.write("""
                 """)
        st.write("""
        1. The `StandardScaler` is applied to the dataset, transforming each feature (pollutants and geographical coordinates) so that they have a mean of 0 and a standard deviation of 1.
        2. Normalization ensures that all the variables (pollutants like `pm25`, `pm10`, etc.) are on the same scale. This is crucial when applying algorithms like KMeans and PCA, as they are sensitive to feature scales.
        3. Below is the first five rows of the normalized pollutant data.

        """)
        st.image("Images/Cluster6.png", use_column_width=True, caption="Dataset After Normalization")
        st.write("""
                 """)
        
        st.write("""
        1. The data was reduced to 3 principal components (`PC1`, `PC2`, `PC3`). These components capture the maximum variance in the data while lowering the complexity of the dataset.
        2. **Why Use PCA?** PCA helps to simplify the data, making it easier to visualize and process, especially when dealing with high-dimensional datasets. It retains the most significant information while reducing redundant features.
        3. Below is the first five rows of the data after applying PCA, with the resulting principal components.

        """)
        st.image("Images/Cluster7.png", use_column_width=True, caption="PCA-Transformed Data")
        st.write("""
                 """)
        st.image("Images/Cluster8.png", use_column_width=True, caption="PCA-Transformed Data")
        st.write("""
        The image above shows the cumulative variance explained by the first three principal components of the dataset. After applying PCA (Principal Component Analysis), it was determined that the first three principal components explain approximately **71%** of the total variance present in the data.
        """)

        st.markdown("#### Code and Results")
        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Clustering.ipynb)", unsafe_allow_html=True)
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)", unsafe_allow_html=True)
        
        st.markdown("#### K-Means Clustering")
        st.image("Images/Cluster9.png", use_column_width=True, caption="Silhouette Scores for Different K")
        # Explanation
        st.write("""
        In this part of the analysis, the **Silhouette Score** is used to determine the optimal number of clusters (`k`) for KMeans clustering. The Silhouette Score quantifies how well points are clustered by calculating how similar a point is to its own cluster compared to other clusters.

        The plot illustrates the **Silhouette Scores** for `k=2`, `k=3`, `k=4`, `k=5`, and `k=6`. Higher score values indicate better clustering, meaning that points are more distinct and well-grouped within their respective clusters.

        It is observed from the graph that the highest silhouette scores are achieved for `k=2`, `k=3`, and `k=5`. Therefore, these values of `k` are selected for further analysis. These values provide the best balance between cluster separation and compactness, which are key criteria for effective clustering. This process ensures that the chosen clusters represent the most meaningful divisions within the dataset.
        
        Due to the large number of data points, the computation required for this analysis was time-intensive.
        """)
        st.write("""
                 """)
        st.image("Images/Cluster10.png", use_column_width=True, caption="Plots FOR K = 3, K= 5 AND K =7")
        st.write("""
        The figure illustrates the 3D KMeans clustering results for three different values of `k` (number of clusters): `k=2`, `k=3`, and `k=5`, which were determined to be optimal using the **Silhouette Score** method. The clustering has been performed on the PCA-reduced 3D data, representing the most important dimensions (principal components).

        Each plot shows the distinct clusters formed by KMeans, with cluster centroids marked by **red "X"** symbols. These centroids represent the central points of each cluster, calculated by the KMeans algorithm based on minimizing the variance within clusters.

        - **For k=2**: The data is split into two primary clusters, with a large cluster on one side and a smaller one on the opposite. This clustering seems to capture broad distinctions within the dataset.
        - **For k=3**: A third cluster emerges, indicating that more granular divisions are being captured by the model, and the data shows slightly improved separability.
        - **For k=5**: Five clusters show more detailed separation, allowing for a deeper understanding of the patterns and groupings within the dataset.

        The plots allow for a visual comparison of how the data is divided for each value of `k`. Increasing `k` results in finer divisions of the data, but it is important to balance granularity with interpretability. 
        """)

        st.markdown("#### Hierarchical Clustering")
        st.write("""
        Hierarchical clustering is a method used to build a hierarchy of clusters in a dataset by either iteratively merging or splitting clusters based on their proximity. In this project, the **Ward's method** is utilized, which minimizes the variance within each cluster. 

        Due to memory constraints, only 10,000 samples were selected from the dataset to generate the dendrogram. The dendrogram, displayed below, provides a visual representation of how clusters are merged at different distances. Each branch of the dendrogram represents a cluster, and the length of the branches (height) indicates the distance between clusters at the time of merging. Clusters are formed by cutting the dendrogram at a specific distance, which will result in a certain number of clusters based on how many branches are cut.

        """)
        st.image("Images/Cluster11.png", use_column_width=True, caption="Dendrogram for Hierarchical Clustering")
        st.write("""
        The dendrogram reveals that two main clusters are formed at a larger distance, with smaller sub-clusters being identified as we move down the hierarchy. This provides insight into the natural grouping of the data points, as well as how close or distant different clusters are. The hierarchical clustering structure can be leveraged to decide the number of clusters in further analysis or to visualize the relationships between the clusters at different levels of granularity.
        """)
        st.write("""
        The hierarchical clustering results, as visualized by the dendrogram, can be compared to the **KMeans clustering** results in several key ways:

        1. **Number of clusters**: In hierarchical clustering, the number of clusters is determined by cutting the dendrogram at a certain distance. The KMeans approach, however, requires the number of clusters (`k`) to be specified in advance. In this case, the optimal number of clusters for KMeans was determined using the silhouette score, selecting `k=2`, `k=3`, and `k=5`, while the dendrogram provides a more dynamic range of possible clusters.

        2. **Cluster hierarchy**: The dendrogram offers a clear hierarchy of clusters, showing how smaller clusters combine into larger ones at different distances. KMeans, on the other hand, provides distinct and non-hierarchical clusters, where data points are grouped solely based on proximity to centroids. This means that hierarchical clustering gives more flexibility for visualizing clusters at different granularities, while KMeans creates flat, non-overlapping clusters.

        3. **Cluster structure**: KMeans clustering is centroid-based and tends to create spherical clusters. The dendrogram, however, suggests a more hierarchical and flexible grouping that may accommodate non-spherical cluster shapes better. This hierarchical structure is useful in cases where the data contains nested or irregularly shaped clusters.

        4. **Scalability**: Hierarchical clustering, particularly the Ward method used here, is computationally more expensive than KMeans, especially for larger datasets. As noted, memory constraints limited the hierarchical clustering to 10,000 samples, whereas KMeans was applied to the entire dataset. This makes KMeans a more practical choice for large-scale clustering tasks, although hierarchical clustering offers deeper insights into cluster relationships.

        Overall, while KMeans provides efficient and well-separated clusters, hierarchical clustering offers a broader perspective on how the data clusters evolve, making it a valuable method for exploring the structure of the data at different levels.
        """)

        st.markdown("#### DBSCAN")
        st.write("""
        In this part of the project, **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** is applied to the PCA-transformed dataset. Unlike KMeans, which creates clusters based on predefined centroids, DBSCAN identifies clusters based on the density of points, making it ideal for finding clusters of varying shapes and sizes, as well as detecting outliers.

        The plot illustrates the results of applying DBSCAN to the 3D PCA data. Each point represents a data sample, and the colors indicate the cluster labels assigned by the DBSCAN algorithm. DBSCAN can identify points that do not belong to any cluster (outliers) and label them as -1 (not visible in this case). A color bar is added to indicate which color corresponds to each cluster label.

        Since DBSCAN does not require the number of clusters (`k`) to be predefined, it is particularly useful for datasets where the number of clusters is unknown or varies across the data. The algorithm groups closely packed points into clusters and treats points in low-density regions as noise.
        """)
        st.image("Images/Cluster12.png", use_column_width=True, caption="DBSCAN Clustering")

        st.write("""
        **KMeans** clustering performed effectively in forming well-defined, spherical clusters, as evidenced by the relatively high silhouette scores. The method successfully grouped data into distinct clusters, especially for the chosen `k=2`, `k=3`, and `k=5`, where the silhouette scores indicated strong cluster separation. The clusters were compact, and the centroids were easily identified, making KMeans a reliable choice when the number of clusters is known or can be determined through evaluation metrics like the silhouette score.

        **Hierarchical Clustering**, on the other hand, provided a deeper understanding of the data by uncovering relationships at multiple levels of granularity. Through the dendrogram, it was possible to see how clusters are formed progressively, from individual points to larger groupings. This method is particularly useful for exploring hierarchical relationships in the data and can reveal nested structures that are not immediately apparent in flat clustering methods like KMeans. However, it is more computationally expensive and may struggle with large datasets.

        **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) offered a different perspective by detecting clusters based on density rather than centroids or distance. One of DBSCAN's strengths is its ability to identify noise and outliers, which is a significant advantage over KMeans and Hierarchical Clustering, both of which assign every point to a cluster. However, while DBSCAN excels at handling irregularly shaped clusters and noise, the resulting clusters were less well-defined than those produced by KMeans. The effectiveness of DBSCAN also heavily depends on selecting the right hyperparameters (`eps` and `min_samples`), which can be challenging and may require experimentation.

        In conclusion, each clustering method brings its own strengths:
        
        - **KMeans** is ideal for datasets where clusters are approximately spherical, and the number of clusters is known or can be inferred.
        - **Hierarchical Clustering** offers insight into how clusters are related at different levels, revealing the data's structure at varying degrees of granularity.
        - **DBSCAN** is well-suited for detecting noise and irregularly shaped clusters, making it useful for datasets with outliers or varying densities.

        The choice of the clustering algorithm ultimately depends on the nature of the data and the goals of the analysis. In this project, KMeans provided the clearest clustering results with well-defined groups, while Hierarchical Clustering allowed for an exploration of relationships within the data. DBSCAN added value by identifying noise and outliers, which the other methods could not detect as effectively.
        """)

        st.markdown("#### Learnings")
        st.write("""

        The analysis of global air quality highlighted important trends and patterns that can help shape future environmental actions:

        - **Diverse Pollution Levels:** Air pollution varies significantly across cities and regions. Understanding these variations is crucial for addressing the unique challenges faced by both densely populated urban areas and smaller, rural regions. This knowledge can guide governments and organizations in targeting their efforts to improve air quality where it’s needed the most.

        - **The Role of Clustering:** By grouping cities with similar pollution levels, we can identify trends that go beyond individual locations. This kind of information can help policymakers focus on regional solutions to improve air quality rather than adopting a one-size-fits-all approach.

        - **Seasonal and Geographic Patterns:** The data shows that air quality changes with the seasons and is influenced by factors like population density and industrial activity. A deeper understanding of these trends could help cities prepare for periods of poor air quality and take proactive steps to protect public health.

        - **Visualizing the Big Picture:** Simplifying complex data helps to better understand the overall trends. This approach makes it easier to communicate findings and make informed decisions about improving air quality for everyone.

        - **Real-World Impact:** These insights can empower local authorities and environmental groups to prioritize their efforts, focusing on the most pressing pollution issues. It also highlights the need for continued monitoring and action to create healthier and cleaner environments for communities across the world.

        In conclusion, this project demonstrates the importance of using data to understand and address the complex issue of air pollution. Through collaboration and targeted action, there is the potential to make significant improvements in the air we breathe.
        """)
    
    elif sub_tab == "Association Rule Mining":
        st.subheader("Association Rule Mining")
        st.write("""
        ##### Overview

        Association Rule Mining (ARM) is a powerful data mining technique used to identify patterns and relationships within large datasets, particularly in transaction data. Its main goal is to discover interesting associations between items or itemsets, providing actionable insights for various fields such as retail, marketing, and healthcare.

        ##### Key Measures in ARM

        1. **Support**:
            - Support measures the frequency with which an item or itemset appears in the dataset. It helps to determine how often a particular item occurs and filter out irrelevant or rare itemsets that may not provide useful insights.
            - Support(A) = (Transactions containing item A) / (Total transactions)
            - Higher support indicates that an item or itemset is more frequent.
        """)
        # Image for Support
        st.image("Images/ARM1.png", use_column_width=True, caption="Support Formula")

        st.write("""
        2. **Confidence**:
            - Confidence measures the strength of the association between itemsets. Specifically, it calculates how often item B appears in transactions that contain item A.
            - Confidence(A → B) = (Transactions containing both A and B) / (Transactions containing A)
            - Higher confidence means a stronger relationship between the items.
        """)
        # Image for Confidence
        st.image("Images/ARM2.png", use_column_width=True, caption="Confidence Formula")

        st.write("""
        3. **Lift**:
            - Lift evaluates the strength of an association rule by considering the co-occurrence of items relative to their independent frequencies. A lift value greater than 1 indicates a positive association between the items.
            - Lift(A → B) = Support(A, B) / (Support(A) × Support(B))
            - A higher lift value indicates that item B is more likely to occur when item A is present, compared to a random occurrence.
        """)
        # Image for Lift
        st.image("Images/ARM5.png", use_column_width=True, caption="Lift Formula")

        st.write("""
        ##### Association Rules

        Association rules capture co-occurrence relationships between itemsets in the form {A} → {B}, where A is the antecedent and B is the consequent. These rules are valuable for identifying patterns such as "if a customer buys item A, they are likely to buy item B." For example, the rule {Bread, Butter} → {Milk} suggests that customers who purchase bread and butter are also likely to purchase milk. Association rules are vital for decision-making, such as product placement or marketing strategies.
        """)
        # Conceptual image for ARM
        st.image("Images/ARM3.png", use_column_width=True, caption="Concepts of Association Mining")

        st.write("""
        ##### Apriori Algorithm

        The **Apriori Algorithm** is a foundational algorithm for discovering frequent itemsets and generating association rules. It follows a "bottom-up" approach, where frequent itemsets are extended one item at a time. The algorithm works in two main stages:

        1. **Frequent Itemset Generation**:
            - **Candidate Generation**: Initially, the algorithm identifies all individual items in the dataset and calculates their support. Items meeting the minimum support threshold are considered frequent.
            - **Candidate Pruning**: In each iteration, new itemsets are generated by combining previously identified frequent itemsets. Itemsets that do not meet the minimum support threshold are discarded.

        2. **Association Rule Generation**:
            - Once frequent itemsets are identified, association rules are generated by splitting itemsets into antecedent and consequent parts. Metrics such as support, confidence, and lift are calculated to evaluate the quality of these rules.

        The Apriori Algorithm is efficient due to its pruning strategy, where only frequent itemsets are expanded to larger ones.
        """)
        # Image for Apriori Algorithm
        st.image("Images/ARM4.png", use_column_width=True, caption="Apriori Algorithm")
        st.write("""
        The visualization above demonstrates how the **Apriori Algorithm** is applied to a dataset, specifically showing relationships between various items in transactions. The Apriori Algorithm is used here to identify frequent itemsets and association rules, helping to uncover patterns such as which items are commonly purchased together.

        - **Nodes**: Each node represents an item, such as "whole milk," "yogurt," or "tropical fruit." The size of the node indicates the frequency of the item, where larger nodes represent items with higher support (i.e., items that appear in a larger proportion of transactions).
        - **Arrows**: The arrows represent **association rules** derived from frequent itemsets. They show the direction of the rule, indicating that when the items on the left-hand side (antecedent) are purchased, the items on the right-hand side (consequent) are likely to be purchased as well.
        - **Colors**: The color intensity reflects different confidence levels for each rule. Darker colors indicate higher confidence, meaning a stronger relationship between the antecedent and consequent.

        This visualization helps to understand how items are associated in transactions and how the Apriori Algorithm can be used to drive strategies such as product placement, marketing campaigns, or targeted promotions.
        """)
        st.write("""
        """)
        st.write("""
        In this project, **Association Rule Mining (ARM)** was applied to explore relationships between pollutants and their levels across different locations. The **Apriori Algorithm** was used to identify frequent pollutant combinations and generate association rules. The key measures (Support, Confidence, and Lift) were used to filter out significant relationships, offering insights into how certain pollutants co-occur in various regions.

        The findings from ARM could be crucial for policymakers and environmental agencies, guiding their decisions on air quality management, especially in areas where multiple pollutants are present at concerning levels.
        """)

        st.markdown("#### Data Preperation")
        


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
st.write("© 2024 Yashwanth Reddy Thallapalli")
