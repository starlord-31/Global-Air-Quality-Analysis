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
        st.image("Images/20240908_235437.jpg", caption="This is me!")

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
        sub_tab = st.selectbox("Choose a topic", ["Introduction", "Data Gathering", "Data Prep/EDA", "PCA", "Clustering", "Association Rule Mining", "Naïve Bayes", "Decision Tree", "Regression", "Conclusions"])

    if sub_tab == "Introduction":
        st.subheader("Introduction")
        st.write("""
Air quality has become one of the most pressing environmental challenges of the 21st century. Rapid urbanization, industrial growth, and a burgeoning global population have led to unprecedented levels of pollution, significantly affecting the air we breathe. Poor air quality is strongly linked to a variety of health problems, ranging from respiratory diseases such as asthma, chronic obstructive pulmonary disease (COPD), and bronchitis, to cardiovascular conditions and even premature death. The World Health Organization (WHO) reports that millions of premature deaths occur every year due to outdoor air pollution, emphasizing the critical impact it has on global public health. Beyond its impact on human health, deteriorating air quality has severe economic implications, such as rising healthcare costs, diminished workforce productivity, and loss of biodiversity, making it a focal issue for policymakers, public health advocates, and economic planners across the globe.        """)

        st.write("""
Among the major air pollutants of concern are particulate matter, particularly PM2.5 and PM10, which can penetrate deep into the lungs and even enter the bloodstream, leading to long-term health issues. Gaseous pollutants like carbon monoxide (CO), nitrogen dioxide (NO2), sulfur dioxide (SO2), and ozone (O3) also contribute substantially to air pollution's harmful effects, impacting human health, ecosystems, and climate stability. Long-term exposure to these pollutants can lead to severe chronic diseases and accelerate the effects of climate change. The interactions between pollutants, their sources, and environmental factors such as weather conditions make air pollution a complex challenge to tackle. This complexity necessitates the use of data-driven approaches to thoroughly understand and effectively mitigate the impacts of air pollution on society.        """)

        st.write("""
In this project, air quality data from key cities worldwide, including urban centers such as London, Delhi, Denver, and Beijing, are analyzed to understand patterns in air pollution from 2007 to 2024. These cities were chosen due to their diverse geographical, climatic, and economic conditions, allowing for a comprehensive comparative analysis of air pollution trends. For instance, London, a city with a significant industrial history and recent emphasis on green energy initiatives, highlights the challenges of combating pollution from urban traffic and industry. Meanwhile, Delhi, one of the most polluted cities globally, faces acute issues related to vehicular emissions, coal burning, and agricultural residue burning. The contrasting scenarios presented by these cities provide valuable perspectives on how different factors contribute to air pollution and offer potential pathways for intervention.        """)

        st.write("""
Beyond analyzing pollutant concentrations, this project applies advanced data analysis techniques, including Principal Component Analysis (PCA) and clustering algorithms, to reveal the underlying drivers and patterns of air pollution. PCA helps reduce the dimensionality of the data and simplifies complex relationships between pollutants, allowing for clearer insights into the principal factors contributing to air quality variations. Clustering techniques such as KMeans, hierarchical clustering, and DBSCAN are employed to identify natural groupings within the data, uncovering patterns related to geography, economic activity, and seasonal variations. These techniques offer a richer, data-driven perspective on how and why air pollution levels fluctuate across different regions and periods, enabling more effective targeting of mitigation strategies.
        """)
        st.write("""
The temporal dynamics of air quality are another critical focus of this project. Understanding how pollution levels change over time and in response to policy measures, economic shifts, and seasonal variations provides actionable insights for public health officials and policymakers. Seasonal spikes in pollution due to agricultural practices, year-round industrial emissions, and other factors are explored in depth. Additionally, the interactions and synergies between different pollutants are investigated, as certain combinations can exacerbate their harmful effects. By offering a holistic, data-driven analysis of air quality trends, this project aims to inform urban planning, environmental policy, and public health interventions aimed at reducing exposure to air pollution and mitigating its harmful effects on human health and the environment.
        """)
        
        st.subheader("Motivation")
        st.write("""
        The motivation for this project arises from the urgent need to better understand and address air pollution's significant impact on urban populations worldwide. With millions of premature deaths linked to air pollution annually, identifying the patterns and sources of pollution is essential for effective policymaking and mitigation strategies. This project aims to provide a detailed analysis of air quality data, shedding light on the main contributors to pollution and uncovering trends across various cities.
        """)

        st.write("""
        By applying advanced data analysis techniques, we seek to generate actionable insights that can guide public health interventions, environmental policies, and sustainable urban development efforts. Understanding how factors such as population density, economic activities, and geographic characteristics influence pollution levels will enable more targeted and effective approaches to reduce air pollution and protect public health.
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

        st.image("Images/poll.jpg", use_column_width=False)

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
        st.image("Images/15.png", use_column_width=True, caption="Cleaned Dataset")

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
        #### Overview

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
        #### Overview

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
        #### Association Rules

        Association rules capture co-occurrence relationships between itemsets in the form {A} → {B}, where A is the antecedent and B is the consequent. These rules are valuable for identifying patterns such as "if a customer buys item A, they are likely to buy item B." For example, the rule {Bread, Butter} → {Milk} suggests that customers who purchase bread and butter are also likely to purchase milk. Association rules are vital for decision-making, such as product placement or marketing strategies.
        """)
        # Conceptual image for ARM
        st.image("Images/ARM3.png", use_column_width=True, caption="Concepts of Association Mining")

        st.write("""
        #### Apriori Algorithm

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
        # Explanation for transforming the dataset
        st.write("""
        Association Rule Mining (ARM) requires the data to be in a **transactional format**, where each row represents a "transaction" and each column represents the presence or absence of an item. In this case, the dataset consists of air quality data where each row corresponds to a pollution measurement event, and each pollutant (e.g., pm25, no2) is considered as an item.
            
        To prepare the dataset for ARM analysis, the following steps were applied:
        1. **Binning**: The pollutant concentrations were categorized into bins such as 'Low', 'Medium', and 'High', which provides a more interpretable format for ARM.
        2. **One-Hot Encoding**: Each pollutant level (e.g., `pm25_Low`, `no2_High`) is treated as a distinct item. One-hot encoding converts these categorical pollutant levels into a binary matrix, where `1/True` represents the presence of the specific pollutant level in a measurement event, and `0/False` represents its absence.

        This transformation helps ARM identify the frequent co-occurrences of pollutant levels across different events, allowing for the discovery of meaningful patterns between pollutant levels.
        """)

        # Display the original dataset image
        image_path_original = "Images/15.png" 
        st.image(image_path_original, use_column_width=True, caption="Original Dataset Before Transformation")

        # Display the binary dataset image
        image_path_encoded = "Images/ARM6.png"
        st.image(image_path_encoded, use_column_width=True, caption="Binary Transactional Dataset After Transformation")

        # Conclusion for data transformation
        st.write("""
        The binary transactional dataset allows the application of **Association Rule Mining** techniques such as the Apriori algorithm, which helps in discovering frequent co-occurring patterns of different pollutant levels (Low, Medium, High). The transformation provides a clear view of which pollutant categories appear together, thus facilitating the analysis of air quality patterns.

        This method helps to uncover important rules, like whether a certain level of pm25 is likely to occur alongside elevated levels of other pollutants such as no2 or so2. These insights can be crucial for understanding air pollution dynamics and providing actionable insights for environmental policy-making.
        """)

        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/ARM.ipynb)", unsafe_allow_html=True)
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)", unsafe_allow_html=True)

        st.markdown("#### Results and Analysis")
        st.write("""
        ##### Top Rules Identification
        The analysis through **Association Rule Mining (ARM)** identified significant relationships between different pollutant levels in the dataset. Using specific thresholds, the strongest associations between pollution measurements were extracted. These relationships offer crucial insights into how various pollutants co-occur in the atmosphere, helping to inform policies on air quality control and pollution mitigation.

        ##### Thresholds Used:
        - **Support Threshold**: 0.02 (minimum percentage of transactions where the itemset appears)
        - **Confidence Threshold**: 0.35 (minimum expected likelihood of the consequent itemset occurring when the antecedent is present)

        These thresholds were selected to capture the most relevant and meaningful patterns in the data. The top 15 rules for **support**, **confidence**, and **lift** were extracted and visualized.
        """)

        # Display for Top 15 Rules by Support
        st.write("""
        ##### Results by Support:
        Support refers to the frequency with which an itemset appears in the dataset. In this analysis, the top 15 rules with the highest support were identified, showcasing which pollutant combinations most frequently occur together.
        """)

        # Add the image for Top 15 Rules by Support
        st.image('Images/ARM7.png', caption='Top 15 Rules by Support', use_column_width=True)
        st.write("##### Insights from Support-based Rules:")
        st.write("""
        - The most frequent association involves **pm25** and **pm10** levels. This is expected because both pollutants are commonly measured and tend to correlate in air quality datasets.
        - The highest support value of 0.059 suggests that around 6% of the measurement events exhibit a correlation between **no2_Medium** and **o3_High**, indicating that these pollutants often appear together in significant quantities.
        - High-support rules suggest widespread patterns that could help in designing air quality control strategies, where tackling one pollutant may automatically reduce the presence of another.
        """)
        # Display for Top 15 Rules by Confidence
        st.write("""
        ##### Results by Confidence:
        Confidence measures how often item B appears in transactions that contain item A. The top 15 rules with the highest confidence were extracted, reflecting the strongest relationships between antecedent and consequent pollutant levels.
        """)

        # Add the image for Top 15 Rules by Confidence
        st.image('Images/ARM8.png', caption='Top 15 Rules by Confidence', use_column_width=True)
        st.write("##### Insights from Confidence-based Rules:")
        st.write("""
        - **o3_Low and so2_Low → no2_Low** is the highest-confidence rule, with a confidence of 0.71, meaning that when **o3** and **so2** levels are low, there is a 71% chance that **no2** will also be low.
        - Many high-confidence rules involve combinations of low pollutant levels, which suggests that the presence of one pollutant at low levels often corresponds to others being low as well.
        - The high-confidence rules are crucial for predicting air quality: they suggest reliable conditions where multiple pollutants can be effectively managed together.
        """)
        # Display for Top 15 Rules by Lift
        st.write("""
        ##### Results by Lift:
        Lift is a measure of how much more likely item B is to appear when item A is present compared to when B appears independently. A higher lift value indicates a stronger association. The top 15 rules with the highest lift values provide the most significant insights into the co-occurrence patterns of pollutants.
        """)

        # Add the image for Top 15 Rules by Lift
        st.image('Images/ARM9.png', caption='Top 15 Rules by Lift', use_column_width=True)
        st.write("##### Insights from Lift-based Rules:")
        st.write("""
        - The rule **no2_Low and o3_Low → so2_Low** has the highest lift of 6.45, which indicates that the presence of **no2_Low** and **o3_Low** increases the likelihood of **so2_Low** by over 6 times.
        - High-lift rules identify pollutant combinations that are more likely to co-occur than expected by chance, revealing strong interdependencies between these pollutants.
        - These associations may reflect atmospheric or environmental factors that cause certain pollutants to move together. For instance, regulatory or weather conditions may favor these joint reductions.
        """)
        st.write("""
        ##### Scatter Plot: Association Rules (Support vs Confidence)
        The scatter plot below visualizes the relationship between **support** and **confidence**, with the size and color of the points representing the **lift** values. Larger and darker circles indicate higher lift values, representing stronger associations.
        """)
        st.image('Images/ARM10.png', caption="Scatter Plot: Support vs Confidence", use_column_width=True)
        st.write("""
        ##### Insights from Scatter Plot:
        - The largest rule based on lift involves **so2_Low** and **no2_Low**, which appears prominently due to its high lift and strong confidence. This rule is highly likely to occur in most cases.
        - Points that are both large and high on the y-axis (confidence) indicate reliable associations that can be used to forecast pollutant behaviors.
        - A positive relationship between support and confidence is observed, meaning that frequent associations tend to be more reliable.
        """)
        # Network of Association Rules visualization
        st.write("""
        ##### Network of Association Rules
        The network graph below depicts the relationships between different pollutant levels, where the nodes represent pollutants, and the edges (arrows) represent the association rules. The thickness of the edges corresponds to the support of the rules, and the labels indicate the confidence and lift values.
        """)
        st.image('Images/ARM11.png', caption="Network of Association Rules", use_column_width=True)
        st.write("""
        ##### Insights from Network Visualization:
        - The network clearly shows how **co_Low** serves as a central node, meaning that **co_Low** frequently appears with other pollutants. This suggests that interventions focusing on reducing **co** may positively affect other pollutants.
        - The thickest edges in the network correspond to the most frequent associations (i.e., high support values), making them key targets for policy and regulatory decisions.
        - The rule **o3_Low, so2_Low → no2_Low** stands out due to its high confidence and lift values, making it one of the most actionable patterns in this dataset.
        """)

        st.write("""
        #### Conclusion

        This Association Rule Mining analysis provided a deeper understanding of the co-occurrence of different pollutants. The results offer valuable insights:

        1. **High-support rules** identify widespread pollutant patterns that could inform public health initiatives and environmental regulations.
        2. **High-confidence rules** suggest reliable co-occurrences, aiding in the prediction of air quality conditions.
        3. **High-lift rules** uncover strong, non-random associations, suggesting key pollutant interdependencies that are useful for targeted interventions.

        By analyzing these relationships, environmental agencies can prioritize the most impactful strategies for improving air quality, focusing on pollutant pairs that tend to occur together.
        """)

        st.write("""
        #### Learnings

        The Association Rule Mining (ARM) analysis of air pollutant data uncovered critical insights into the relationships between various pollutant levels such as **PM2.5**, **PM10**, **NO2**, **SO2**, **O3**, and **CO**. These associations provide a deeper understanding of how certain pollutants co-occur, which can guide strategies for air quality management, pollution control, and public health initiatives.

        ##### Key Insights on Pollutant Associations:
        The ARM analysis revealed strong co-occurrences among several pollutant levels, helping to identify which pollutants are likely to occur together under specific environmental conditions.

        - **Low levels of multiple pollutants often occur together**: The most frequent rules identified suggest that low levels of pollutants like **SO2**, **NO2**, and **O3** tend to occur simultaneously. This pattern suggests that regions or periods with lower industrial or vehicular activity likely see a general reduction in air pollution.
        - **CO as a central pollutant**: The analysis revealed that **CO_Low** serves as a central node in many association rules. This implies that reductions in **CO** levels are often accompanied by reductions in other pollutants, making it a key target for improving overall air quality.
        
        ##### Influence of Pollutant Relationships:
        The relationships uncovered between pollutants have important implications for air quality management:

        - **Simultaneous Reduction of Multiple Pollutants**: Reducing levels of one pollutant, such as **CO**, may have the added benefit of lowering other pollutants. This co-reduction pattern can help policymakers design more efficient air quality management strategies, targeting multiple pollutants simultaneously.
        - **Pollutant Buildup and Weather Conditions**: The strong associations between **NO2**, **SO2**, and **O3** suggest that weather conditions like high pressure or temperature inversions could cause certain pollutants to accumulate together. Understanding these patterns can guide public warnings during pollution spikes.

        ##### Regional Air Quality Management:
        These insights can help tailor air quality policies to specific regions or cities by understanding their unique pollutant combinations and environmental factors.

        - **Targeted Interventions**: For example, regions with high co-occurrence of **SO2** and **NO2** might require more stringent controls on industrial emissions, while areas with high **O3** could benefit from traffic reduction measures.
        - **Seasonal Patterns**: The associations revealed could also help predict seasonal pollution patterns, as certain combinations of pollutants are more prevalent during particular weather conditions or seasons.

        ##### Supporting Sustainable Urban Development:
        The patterns identified through ARM can inform sustainable urban development by focusing efforts on reducing emissions from key sources and improving air quality in densely populated areas.

        - **Informed Public Health Strategies**: By understanding which pollutants tend to spike together, public health officials can better predict periods of poor air quality and issue timely advisories to protect vulnerable populations.
        - **Supporting Policy Decisions**: The insights gained from this analysis can inform long-term policy decisions aimed at reducing pollutant concentrations and improving air quality, which is essential for sustainable urban planning.

        In conclusion, the ARM analysis provided essential insights into pollutant interactions and co-occurrences, revealing patterns that can guide more effective air quality interventions. By targeting the most frequent and impactful pollutant combinations, stakeholders can create more robust environmental policies and public health strategies to reduce air pollution and protect communities from the adverse effects of poor air quality.
        """)


    elif sub_tab == "Naïve Bayes":
        st.image("Images/Naive1.png", caption="Overview of Naïve Bayes Classification", use_column_width=True)
        st.write("#### Overview")
        st.write("""
            **Naïve Bayes (NB)** is a simple, yet powerful, machine learning algorithm used for classification tasks. It is based on **Bayes' Theorem**, which 
            calculates the probability of a class based on prior knowledge of conditions related to that class. The key assumption of Naïve Bayes is that 
            features are independent of each other given the class label. While this "naïve" assumption may not always hold true in real-world scenarios, it 
            significantly simplifies calculations, making Naïve Bayes efficient and scalable, especially for large datasets.
            
            Naïve Bayes is widely used for tasks such as **text classification**, **spam detection**, **sentiment analysis**, and **recommendation systems** due 
            to its simplicity, fast computation, and reasonable accuracy.
        """)
        # Display an overview image
        st.image("Images/Naive2.png", caption="Bayes' Theorem", use_column_width=True)

        st.write("#### Variations of Naïve Bayes")
        st.write("""
            There are several variations of the Naïve Bayes algorithm, each tailored to different data types and use cases:
        """)

        st.image("Images/Naive3.png", caption="Overview of Naïve Bayes Variations", use_column_width=True)

        st.write("##### 1. Multinomial Naïve Bayes (MNB)")
        st.write("""
            - The **Multinomial Naïve Bayes** algorithm is best suited for **discrete data**. It is widely used in **text classification** tasks, where features 
            represent word counts or frequencies.
            - This variation assumes that features (e.g., word counts) follow a multinomial distribution, making it well-suited for scenarios like spam detection, 
            where the frequency of words matters.
            - **Smoothing in MNB**: To handle cases where a word appears in the test set but not in the training set (resulting in zero probabilities), 
            **Laplace smoothing (also known as additive smoothing)** is applied. Smoothing ensures that zero probabilities are avoided, preventing the entire 
            probability from becoming zero due to one missing feature.
        """)

        st.write("##### 2. Gaussian Naïve Bayes (GNB)")
        st.write("""
            - **Gaussian Naïve Bayes** is designed for **continuous data** and assumes that the features follow a **Gaussian (normal) distribution**.
            - This makes it suitable for datasets with continuous variables, such as measurements or sensor data.
            - The algorithm calculates the probability of a feature belonging to a class using the **probability density function of the Gaussian distribution**.
        """)

        st.write("##### 3. Bernoulli Naïve Bayes (BNB)")
        st.write("""
            - The **Bernoulli Naïve Bayes** algorithm is suited for **binary/boolean data**, where features take values of **1 (present)** or **0 (absent)**.
            - It is often used for tasks where binary occurrence matters, such as determining whether specific words are present in a document.
            - For example, it is commonly applied to text classification problems where the presence or absence of words (rather than their frequency) is used as 
            a feature.
        """)

        st.write("##### 4. Categorical Naïve Bayes (CNB)")
        st.write("""
            - The **Categorical Naïve Bayes** algorithm is specifically designed for **categorical features**. In this context, features are treated as 
            categories with a finite number of possible values.
            - This approach is useful for datasets where features represent distinct categories, such as colors, brands, or product categories.
        """)

        st.write("#### Summary and Comparisons")
        st.write("""
            In summary, **Naïve Bayes** is a robust and versatile algorithm for **classification problems** due to its simplicity, computational efficiency, and 
            adaptability to different data types. Despite its assumption of feature independence, it often performs well in practice, even when this assumption 
            is violated.
            
            #### Comparison of Naïve Bayes Variations:
            - **Multinomial NB**: Best for text data and word counts. Uses multinomial distribution. Laplace smoothing helps handle zero probabilities.
            - **Gaussian NB**: Suitable for continuous data. Assumes normal distribution.
            - **Bernoulli NB**: Ideal for binary features. Focuses on the presence/absence of features.
            - **Categorical NB**: Designed for categorical features with finite possible values.
            
            By choosing the appropriate Naïve Bayes variation, the algorithm can be tailored to suit the nature of the dataset, achieving 
            accurate and meaningful classification results.
        """)

        st.write("#### Data Preparation for Naïve Bayes Models")
    
        st.write("""
            Proper data preparation is essential for building effective Naïve Bayes models. Since Naïve Bayes is a supervised learning method, it requires labeled 
            data, which means each instance in the dataset must be associated with a known class or target variable. The process includes cleaning data, splitting 
            it into training and testing sets, and adapting the format based on the specific Naïve Bayes variation.
        """)
        
        image_path_original = "Images/15.png" 
        st.image(image_path_original, use_column_width=True, caption="Original Dataset")

        st.write("""
        - The dataset was transformed using `.pivot_table()` to reorganize pollutants as separate columns. This facilitated the analysis by clearly structuring pollutant values against unique locations and timestamps.
        - Essential columns, including pollutant values (`pm25`, `pm10`, `no2`, `so2`, `o3`, `co`), were retained, and rows with missing data were removed to ensure data integrity.
        - Columns such as `latitude` and `longitude` were excluded to streamline the dataset for pollutant-focused analysis.
        - The dataframe index was reset to maintain a clean and sequential structure, simplifying subsequent data handling.
    """)

        st.image("Images/Naive4.png", caption="Dataset after Cleaning", use_column_width=True)

        st.write("""
        - Percentiles were calculated for `pm25` and `pm10` pollutants to divide the data into quantile-based categories. Specifically:
            - The 33rd percentile (`pm25_33` and `pm10_33`) and the 66th percentile (`pm25_66` and `pm10_66`) values were computed.
        - A function was defined to categorize air quality into three levels:
            - **'Low'**: When both `pm25` and `pm10` values are below the 33rd percentile.
            - **'Medium'**: When either `pm25` or `pm10` values fall between the 33rd and 66th percentiles.
            - **'High'**: When `pm25` or `pm10` values exceed the 66th percentile.
        - This categorization logic was applied to the dataset, resulting in a new target column, `air_quality_category`, which can serve as the classification label for modeling.
        - The distribution of the newly created target variable was examined to ensure balanced classes for further analysis.
    """)

        st.image("Images/Naive5.png", caption="Target Variable Distribution", use_column_width=True)

        st.write("""The dataset now looks like this:""")
        st.image("Images/Naive6.png", caption="Prepared Dataset", use_column_width=True)

        st.write("""Features:""")
        st.image("Images/Naive7.png", caption="Prepared Dataset", use_column_width=True)

        st.write("""Target Variable:""")
        st.image("Images/Naive8.png", caption="Prepared Dataset", use_column_width=True)

        st.write("""
    - The target variable, `air_quality_category`, was transformed using label encoding to convert categorical values into numerical format for model compatibility.
    - **Features and Target**: 
        - **Features**: The predictor variables consist of pollutant levels (`pm25`, `pm10`, `no2`, `so2`, `o3`, `co`).
        - **Target**: The encoded air quality category, `air_quality_category_encoded`.
    - **Data Splitting**: 
        - The data was divided into training and testing subsets using an 80-20 split ratio.
        - **80% Training Set**: Used to train the models, capturing patterns and relationships within the data.
        - **20% Testing Set**: Reserved for evaluating the model's performance on unseen data to ensure unbiased assessment and prevent overfitting.
""")

        st.image("Images/Naive9.png", caption="Dimensions of Training and Testing Datasets", use_column_width=True)
        st.image("Images/Naive10.png", caption="X_train Dataset", use_column_width=True)
        st.image("Images/Naive11.png", caption="X_test Dataset", use_column_width=True)
        st.image("Images/Naive12.png", caption="y_train Dataset", use_column_width=True)
        st.image("Images/Naive13.png", caption="y_test Dataset", use_column_width=True)

        st.write("#### Importance of Creating a Disjoint Split")

        st.write("""
        ##### Prevention of Overfitting
        Models trained on data learn specific patterns and relationships from the training dataset. If the same data is used for both training and evaluation, performance metrics can appear artificially inflated due to the model's prior exposure to the data. This situation, referred to as **data leakage**, results in overfitting, where the model may perform exceptionally well on known data but exhibit poor generalization on unseen data. A disjoint split ensures that evaluation occurs on data that has not been seen during training, thus providing an unbiased assessment of model performance and reducing overfitting risk.

        ##### Assessment of Generalization Capability
        Machine learning models must generalize effectively to new and previously unseen data. Using a disjoint test set simulates real-world scenarios where models are deployed to predict or classify novel inputs. For the air quality dataset, this approach enables a robust evaluation of the model's predictive ability on new pollutant measurements, including `pm25`, `pm10`, and other features.

        ##### Validation of Model Robustness
        When models are trained and evaluated on overlapping data, there is a risk that unique characteristics or outliers in the training data may be memorized. This behavior compromises the model's robustness and reliability. Ensuring a disjoint split allows the test set to serve as an unbiased benchmark for evaluating the model's predictions, confirming that predictions are driven by learned patterns rather than noise or specific training artifacts.
        """)

        # Link to code and data
        st.markdown("#### Code and Data")
        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Naïve%20Bayes.ipynb)")
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)")

        st.write("#### Results")
        st.write("#### Gaussian Naive Bayes")
        st.write("""
            Gaussian Naive Bayes (GNB) is applied to classify data by assuming that the features follow a Gaussian distribution. 
            This approach works well for continuous data and is used here to predict air quality categories based on features such as pollutant levels.
            
            The model's performance is evaluated using metrics such as precision, recall, f1-score, and overall accuracy. 
        """)

        # Display the confusion matrix plot (image)
        st.image("Images/Naive14.png", caption="Gaussian Naive Bayes Classification Report and Confusion Matrix")
        st.write("""
    The Gaussian Naive Bayes (GNB) model was applied to predict air quality categories using various pollutant levels as features. 
    The classification report provides key metrics for each category (0: Low, 1: Medium, 2: High air quality):

    - **Accuracy**: The overall accuracy of the model is approximately 86%, indicating that 86% of the predictions made by the model were correct.
    - **Precision, Recall, and F1-Score**: The model shows strong performance across all categories with balanced precision and recall values.
    
    The confusion matrix offers further insights into the model's performance:
    - For **Category 0 (Low)**: The model correctly predicted 2,692 instances as Low, with 512 misclassified as High. 
    - For **Category 1 (Medium)**: The model correctly predicted 2,560 instances as Medium, with 263 misclassified as High.
    - For **Category 2 (High)**: The model correctly classified 4,970 instances as High but had some misclassifications, with 518 predicted as Low and 353 as Medium.

    These results suggest that while the GNB model effectively classifies air quality, there is some degree of overlap and misclassification, 
    particularly between Low and High categories. This might be attributed to similarities in pollutant levels near threshold values.
""")
        
        st.write("#### Multinomial Naive Bayes")
        st.write("""
            Multinomial Naive Bayes (MNB) is specifically designed for handling discrete data and is often used for tasks where features represent counts or frequencies.
            In this analysis, MNB was applied to predict air quality categories using pollutant levels treated as discrete data, aiming to understand how categorical features impact classification.
        """)

        # Display the confusion matrix plot for Multinomial Naive Bayes
        st.image("Images/Naive15.png", caption="Multinomial Naive Bayes Classification Report and Confusion Matrix")

        st.write("""
            The classification report for the Multinomial Naive Bayes (MNB) model on this dataset indicates the following performance:

            - **Accuracy**: The overall accuracy is approximately 40%, which is significantly lower than the Gaussian variant. This lower accuracy reflects MNB's limitations for this dataset, possibly due to its assumption of discrete features not aligning well with the continuous pollutant data.
            - **Precision, Recall, and F1-Score**: The scores show notable variability across the categories, with relatively better precision for category 2 (High) but lower recall for the same category. Categories 0 (Low) and 1 (Medium) have similar but imbalanced metrics, suggesting challenges in correctly differentiating between classes.
            
            The confusion matrix reveals:
            - **Category 0 (Low)**: Of 3,204 instances, 2,514 were correctly classified, but there was substantial misclassification into other categories.
            - **Category 1 (Medium)**: Only 1,102 out of 2,823 instances were correctly identified, showing difficulty in predicting this class accurately.
            - **Category 2 (High)**: 1,154 out of 5,841 instances were correctly classified, with a large number misclassified as Low or Medium.

            The lower accuracy and higher misclassification rates highlight potential mismatches between the MNB assumptions and the characteristics of this dataset, such as pollutant levels not being purely discrete or count-based.
        """)

        st.write("#### Bernoulli Naive Bayes")
        st.write("""
            Bernoulli Naive Bayes (BNB) is tailored for binary/boolean data, focusing on features that indicate the presence (1) or absence (0) of a characteristic. 
            It is often applied in scenarios such as text classification or detecting whether specific attributes exist within a dataset.
        """)

        # Display the confusion matrix plot for Bernoulli Naive Bayes
        st.image("Images/Naive16.png", caption="Bernoulli Naive Bayes Classification Report and Confusion Matrix")

        st.write("""
            The performance of the Bernoulli Naive Bayes (BNB) model on this dataset yielded mixed results:

            - **Accuracy**: The model achieved an accuracy of approximately 51%, which indicates moderate performance. Given the characteristics of the dataset, this could suggest that binary assumptions for pollutant data may not capture the full range of variability inherent in air quality classification.
            - **Precision, Recall, and F1-Score**: The classification report demonstrates notable disparities in precision, recall, and F1-scores across the categories:
                - **Category 0 (Low)**: Precision, recall, and F1-scores are very low, with no correct classifications. This reflects difficulty in accurately predicting this category due to limited binary patterns.
                - **Category 1 (Medium)**: The model shows better performance compared to category 0, but with moderate precision and low recall. Many instances of this category were misclassified as high air quality.
                - **Category 2 (High)**: This category saw a better recall but lower precision, highlighting the model's tendency to correctly identify many high air quality cases, albeit at the cost of incorrectly predicting others.

            The confusion matrix shows:
            - **Category 0** (Low): Most instances were misclassified, showing the limitation of binary assumptions for this category.
            - **Category 1** (Medium): Moderate performance, with substantial misclassifications.
            - **Category 2** (High): Comparatively better classification, although not perfect.

            The Bernoulli Naive Bayes model’s reliance on binary features can limit its effectiveness for datasets like this, where continuous pollutant data may not fit well within strict presence/absence classifications.
        """)

        st.write("#### Comparison of Naive Bayes Models")

        st.write("""
            Three variations of the Naive Bayes algorithm were applied to classify air quality categories based on pollutant data. 
            The models evaluated include Gaussian Naive Bayes, Multinomial Naive Bayes, and Bernoulli Naive Bayes. Each model 
            leverages different assumptions about the data distribution, leading to varying performance outcomes.
        """)

        # Display the comparison bar chart
        st.image("Images/Naive17.png", caption="Accuracy Comparison of Naive Bayes Models")

        st.write("""
            **Model Performance Comparison:**

            - **Gaussian Naive Bayes** achieved the highest accuracy of 86.13%. This model assumes a Gaussian distribution for the data, making it highly suitable for continuous features such as pollutant levels in this dataset. The model demonstrated strong classification performance, as observed in the detailed classification report and confusion matrix.

            - **Multinomial Naive Bayes** performed with an accuracy of 40.19%. This variation assumes that features represent counts or frequencies, which may not align optimally with the distribution of air quality data in this dataset. Consequently, it had difficulty capturing the underlying structure of the data.

            - **Bernoulli Naive Bayes** achieved an intermediate accuracy of 51.41%. The binary representation of features in this model led to moderate performance, with challenges in accurately capturing the continuous nature of pollutant data. Despite its limitations, the model correctly classified a significant portion of the data compared to the Multinomial model.

            The results indicate that the **Gaussian Naive Bayes** model outperforms the others for this dataset, likely due to its ability to handle continuous data effectively. The comparison emphasizes the importance of selecting a model that aligns with the distribution and nature of the dataset's features.
        """)

        st.subheader("Conclusion")

        st.write("""
            The Naive Bayes models provided valuable insights into the classification of air quality levels based on pollutant data:

            **Model Performance:**

            - **Gaussian Naive Bayes** achieved the highest accuracy of 86.13%, making it the most effective model for the continuous features in this dataset. This strong performance highlights that the distribution of pollutants aligns well with the Gaussian assumption, enabling effective classification of air quality categories.
            
            - **Bernoulli Naive Bayes** demonstrated moderate accuracy at 51.41%. While it can effectively handle binary data, it struggled with continuous features such as pollutant concentrations. However, it was still able to make meaningful classifications in some cases.
            
            - **Multinomial Naive Bayes** had the lowest accuracy at 40.19%. Its assumptions of discrete feature distribution limited its performance for this dataset, as it is better suited for count-based data like text classification. The misclassification rates reflect its difficulty in capturing the variability and continuous nature of air pollution data.

            **Insights into Air Quality Classification:**

            - The Gaussian NB model effectively differentiated between "High," "Medium," and "Low" air quality categories, suggesting that key pollutants such as PM2.5, PM10, and other pollutants strongly influence these classifications.
            
            - The confusion matrices revealed that certain categories were more frequently classified correctly, while others exhibited some misclassification, likely due to overlapping distributions of pollutant values.

            **Predictive Applications:**

            - The models can potentially be used to predict air quality levels in different cities based on real-time pollutant data, aiding decision-making for public health measures and pollution control strategies.
            
            - This modeling approach can help identify patterns in air quality trends, such as correlations between specific pollutants and classification categories, which can inform targeted policy interventions.

            **Limitations and Future Work:**

            - While Gaussian NB performed best, further model improvements could involve additional feature engineering to capture complex interactions between pollutants.
            
            - Exploring other machine learning models, such as decision trees or ensemble techniques, could provide a performance benchmark and potentially enhance accuracy.
            
            - Expanding the dataset with additional features such as meteorological data, population density, or geographical information may improve predictive capabilities and provide deeper insights into the factors driving air quality variations.

            **Final Thoughts:**

            Naive Bayes modeling provided a foundational understanding of air quality classification based on pollutant data, with the Gaussian Naive Bayes model emerging as the most effective variation. This analysis lays the groundwork for data-driven strategies and further exploration of air pollution control measures, with room for improvement through advanced modeling and expanded data features.
        """)

    elif sub_tab == "Decision Tree":
        st.write("#### Overview")
        st.write("""
    Decision Trees (DTs) are a widely-used algorithm in machine learning for both **classification** and **regression** tasks. Their structure resembles a tree, with nodes representing decision points based on feature values, branches indicating outcomes, and leaf nodes representing final predictions (either class labels or continuous values). DTs excel due to their **interpretability, flexibility, and ability to handle non-linear relationships** in data. They are used across various domains, including **fraud detection, customer segmentation, and predictive maintenance**.

    **Applications of Decision Trees:**
    - **Classification**: Assigning categorical labels, such as identifying customer segments or predicting disease presence.
    - **Regression**: Estimating continuous values, such as predicting sales figures or stock prices.
    - **Feature Selection**: Determining the most influential variables for prediction.
""")

        # Display an example image of a basic decision tree
        st.image("Images/Tree1.png", caption="Illustration of a Simple Decision Tree", use_column_width=True)

        st.write("""
            **How Decision Trees Are Trained:**
            1. **Feature Selection for Splitting**: At each decision point (node), the algorithm selects the feature that best partitions the data according to a chosen criterion, such as **Gini impurity**, **Entropy**, or **Information Gain**.
            2. **Recursive Partitioning**: The dataset is split repeatedly into subsets until stopping criteria are met (e.g., maximum depth or minimum samples per leaf).
            3. **Leaf Node Assignment**: The final predictions at leaf nodes are based on majority class (classification) or average/median values (regression).

            **How Predictions Are Made:**
            - The trained Decision Tree evaluates input data by traversing from the root node to a leaf node based on the decision rules at each node.
            - The path taken through the tree reflects the feature values in the input data.
        """)

        st.image("Images/Tree2.png", caption="Flowchart of Decision Tree Predictions", use_column_width=True)

        st.write("""
            **Understanding Splitting Metrics: Gini Impurity, Entropy, and Information Gain**

            - **Gini Impurity**: Measures how often a randomly chosen element would be incorrectly classified if it was randomly labeled based on the distribution of labels in the node. Lower Gini values indicate "purer" nodes.
            - Example: In a binary split where 90% of the samples belong to one class, the Gini impurity is low, suggesting a good split.

            - **Entropy**: Represents the degree of randomness or disorder in the data. Lower entropy values signify less randomness and purer splits.
            - Example: If a node contains samples from only one class, the entropy is zero (pure node).

            - **Information Gain**: Quantifies the reduction in impurity after a split and is calculated as the difference between the impurity of the parent node and the weighted impurity of child nodes.
            - Example: A high information gain indicates that a split has effectively separated the data, improving the model's predictive accuracy.
        """)

        st.write("""
    **Example Calculation Using Gini Impurity and Information Gain:**

    Consider a dataset with 120 samples divided into three classes:
    - Class X: 60 samples
    - Class Y: 40 samples
    - Class Z: 20 samples

    **Step 1: Calculate Gini Impurity for the Parent Node**

    - Proportion of Class X: 0.50
    - Proportion of Class Y: 0.33
    - Proportion of Class Z: 0.17

    The Gini Impurity for the parent node is calculated as:
    \n
    `Gini_Parent = 1 - (0.50^2 + 0.33^2 + 0.17^2) = 0.611`

    **Step 2: Perform a Split**

    Assume we split the data as follows:
    - Left Node: 50 samples (30 from Class X, 15 from Class Y, 5 from Class Z)
    - Right Node: 70 samples (30 from Class X, 25 from Class Y, 15 from Class Z)

    **Step 3: Calculate Gini Impurity for Each Child Node**

    - Left Node:
      - Proportion of Class X: 0.60
      - Proportion of Class Y: 0.30
      - Proportion of Class Z: 0.10

      \n
      `Gini_Left = 1 - (0.60^2 + 0.30^2 + 0.10^2) = 0.48`

    - Right Node:
      - Proportion of Class X: 0.43
      - Proportion of Class Y: 0.36
      - Proportion of Class Z: 0.21

      \n
      `Gini_Right = 1 - (0.43^2 + 0.36^2 + 0.21^2) = 0.623`

    **Step 4: Calculate the Weighted Average Gini Impurity of the Child Nodes**

    \n
    `Gini_Children = (50/120) * 0.48 + (70/120) * 0.623 = 0.561`

    **Step 5: Calculate Information Gain**

    \n
    `Information Gain = Gini_Parent - Gini_Children = 0.611 - 0.561 = 0.05`

    This example illustrates how splitting the data into child nodes can reduce the overall impurity, thereby improving the model's classification ability. Information Gain measures the effectiveness of a split, with higher values indicating more meaningful separations of data.
""")
        st.write("""
        **Why Decision Trees Can Grow Indefinitely**

        Decision Trees have the potential to continue splitting the data without limit due to:

        - **Identifying New Feature Combinations and Thresholds:** Trees can explore various combinations of features and find different thresholds for splitting, resulting in deeper subdivisions of the data.
        - **Pursuing Small Differences in Impurity:** Even minute reductions in impurity can prompt further splits, causing the tree to grow increasingly complex.

        While this flexibility allows for a highly tailored model, it may also lead to **overfitting**, where the tree becomes too specific to the training data and fails to generalize to new data. To address this issue, practical Decision Tree implementations often use parameters such as:
        
        - `max_depth`: Limits the maximum depth of the tree.
        - `min_samples_split`: Sets the minimum number of samples required to split a node.
        - `min_samples_leaf`: Specifies the minimum number of samples that must be present in a leaf node.

        By controlling these parameters, it is possible to balance model complexity and performance, avoiding overfitting while maintaining predictive accuracy.
    """)

        st.write("#### Data Preparation")
    
        st.write("""
            Proper data preparation is crucial for building effective Decision Tree models. As a supervised learning method, Decision Trees require labeled data, meaning 
    each instance in the dataset must be associated with a known target or output variable. The preparation process involves cleaning the data, splitting it into 
    training and testing sets, and ensuring features are appropriately formatted for optimal decision-making at each node of the tree. This preparation enables 
    the model to learn and make accurate predictions based on feature splits and hierarchies.
        """)
        
        image_path_original = "Images/15.png" 
        st.image(image_path_original, use_column_width=True, caption="Original Dataset")

        st.write("""
        - The dataset was transformed using `.pivot_table()` to reorganize pollutants as separate columns. This facilitated the analysis by clearly structuring pollutant values against unique locations and timestamps.
        - Essential columns, including pollutant values (`pm25`, `pm10`, `no2`, `so2`, `o3`, `co`), were retained, and rows with missing data were removed to ensure data integrity.
        - Columns such as `latitude` and `longitude` were excluded to streamline the dataset for pollutant-focused analysis.
        - The dataframe index was reset to maintain a clean and sequential structure, simplifying subsequent data handling.
    """)

        st.image("Images/Naive4.png", caption="Dataset after Cleaning", use_column_width=True)

        st.write("""
        - Percentiles were calculated for `pm25` and `pm10` pollutants to divide the data into quantile-based categories. Specifically:
            - The 33rd percentile (`pm25_33` and `pm10_33`) and the 66th percentile (`pm25_66` and `pm10_66`) values were computed.
        - A function was defined to categorize air quality into three levels:
            - **'Low'**: When both `pm25` and `pm10` values are below the 33rd percentile.
            - **'Medium'**: When either `pm25` or `pm10` values fall between the 33rd and 66th percentiles.
            - **'High'**: When `pm25` or `pm10` values exceed the 66th percentile.
        - This categorization logic was applied to the dataset, resulting in a new target column, `air_quality_category`, which can serve as the classification label for modeling.
        - The distribution of the newly created target variable was examined to ensure balanced classes for further analysis.
    """)

        st.image("Images/Naive5.png", caption="Target Variable Distribution", use_column_width=True)

        st.write("""The dataset now looks like this:""")
        st.image("Images/Naive6.png", caption="Prepared Dataset", use_column_width=True)

        st.write("""Features:""")
        st.image("Images/Naive7.png", caption="Features", use_column_width=True)

        st.write("""Target Variable:""")
        st.image("Images/Naive8.png", caption="Target", use_column_width=True)

        st.write("""
    - The target variable, `air_quality_category`, was transformed using label encoding to convert categorical values into numerical format for model compatibility.
    - **Features and Target**: 
        - **Features**: The predictor variables consist of pollutant levels (`pm25`, `pm10`, `no2`, `so2`, `o3`, `co`).
        - **Target**: The encoded air quality category, `air_quality_category_encoded`.
    - **Data Splitting**: 
        - The data was divided into training and testing subsets using an 80-20 split ratio.
        - **80% Training Set**: Used to train the models, capturing patterns and relationships within the data.
        - **20% Testing Set**: Reserved for evaluating the model's performance on unseen data to ensure unbiased assessment and prevent overfitting.
""")

        st.image("Images/Naive9.png", caption="Dimensions of Training and Testing Datasets", use_column_width=True)
        st.image("Images/Naive10.png", caption="X_train Dataset", use_column_width=True)
        st.image("Images/Naive11.png", caption="X_test Dataset", use_column_width=True)
        st.image("Images/Naive12.png", caption="y_train Dataset", use_column_width=True)
        st.image("Images/Naive13.png", caption="y_test Dataset", use_column_width=True)

        st.write("#### Importance of Creating a Disjoint Split")

        st.write("""
        ##### Prevention of Overfitting
        Models trained on data learn specific patterns and relationships from the training dataset. If the same data is used for both training and evaluation, performance metrics can appear artificially inflated due to the model's prior exposure to the data. This situation, referred to as **data leakage**, results in overfitting, where the model may perform exceptionally well on known data but exhibit poor generalization on unseen data. A disjoint split ensures that evaluation occurs on data that has not been seen during training, thus providing an unbiased assessment of model performance and reducing overfitting risk.

        ##### Assessment of Generalization Capability
        Machine learning models must generalize effectively to new and previously unseen data. Using a disjoint test set simulates real-world scenarios where models are deployed to predict or classify novel inputs. For the air quality dataset, this approach enables a robust evaluation of the model's predictive ability on new pollutant measurements, including `pm25`, `pm10`, and other features.

        ##### Validation of Model Robustness
        When models are trained and evaluated on overlapping data, there is a risk that unique characteristics or outliers in the training data may be memorized. This behavior compromises the model's robustness and reliability. Ensuring a disjoint split allows the test set to serve as an unbiased benchmark for evaluating the model's predictions, confirming that predictions are driven by learned patterns rather than noise or specific training artifacts.
        """)

        # Link to code and data
        st.markdown("#### Code and Data")
        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Naïve%20Bayes.ipynb)")
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)")

        st.write("#### Results")
        st.write("""
        The Decision Tree model was applied to the air quality dataset to classify air quality into three categories: Low, Medium, and High. The model operates by 
        recursively splitting data based on feature values (e.g., `pm25`, `pm10`), with each split creating decision nodes and leaf nodes that represent class predictions.
        Decision Trees are effective for modeling complex patterns while remaining interpretable through visual representation.

        #### Model Configurations and Results
        The Decision Tree was evaluated at varying depths to assess its impact on model accuracy and complexity. The configurations and observations are summarized as follows:

        1. **Max Depth = 3**: 
            - This shallow tree structure achieved an accuracy of approximately 99.39%.
            - The model captured essential patterns with a limited number of splits, resulting in high interpretability.
            - However, certain nuances in the data were not captured, leading to some misclassifications, as seen in the confusion matrix.

        2. **Max Depth = 5**: 
            - The model accuracy increased to 99.98%.
            - This configuration balanced capturing intricate decision boundaries while maintaining interpretability.
            - The reduced misclassifications indicate that this depth allowed for better differentiation among the air quality categories without excessive complexity.

        3. **Max Depth = 7**: 
            - Further increasing the depth slightly improved accuracy to 99.99%.
            - The tree became more complex with additional splits, but this added complexity provided minimal performance gains and reduced interpretability.

        ### Visualizations and Confusion Matrices
        The following visualizations and confusion matrices depict the structure and performance of the Decision Tree models at different depths:

        - **Decision Tree (Max Depth = 3)**
        """)
        st.image("Images/Tree3.png", caption="Decision Tree with Max Depth = 3")

        st.write("""
        - **Decision Tree (Max Depth = 5)**
        """)
        st.image("Images/Tree4.png", caption="Decision Tree with Max Depth = 5")

        st.write("""
        - **Decision Tree (Max Depth = 7)**
        """)
        st.image("Images/Tree5.png", caption="Decision Tree with Max Depth = 7")

        st.write("""
        #### Analysis and Key Observations
        - Increasing the tree depth enhanced model accuracy due to improved handling of complex patterns within the data.
        - However, as the depth increased, the added complexity offered diminishing returns, demonstrating the trade-off between interpretability and predictive accuracy.
        - Proper tuning of depth parameters is critical to avoid overfitting, as excessively deep trees may memorize training data instead of generalizing to new inputs.
        - Decision Trees inherently have the potential for infinite growth by continuing to split data into finer distinctions. While this can increase accuracy on the training set, it often results in overfitting and diminished generalization to unseen data. Constraining growth through parameters such as maximum depth, minimum samples per split, and minimum leaf nodes can mitigate this risk and ensure robust, interpretable models.

        The results highlight the effectiveness of Decision Trees for classification tasks, demonstrating a balance between complexity and predictive accuracy when properly tuned.
        """)

        st.write("#### Conclusion")

        st.markdown("##### 1. Key Learnings")
        st.write("""
        The application of Decision Tree models to the air quality classification dataset yielded important insights into the prediction of air quality categories 
        (Low, Medium, High) based on pollutant concentration data.

        **Feature Importance**:  
        - Pollutant concentrations, such as `pm25` and `pm10`, were consistently the most significant predictors of air quality categories, appearing as key decision nodes across different depths.  
        - The consistent importance of these features underscores their strong influence in determining air quality levels.

        **Model Performance**:  
        - Decision Tree models exhibited high accuracy across various configurations, underscoring their suitability for this classification task.  
        - The model with a maximum depth of 3 achieved approximately 99.39% accuracy, striking a balance between simplicity and performance.  
        - Models with greater depths (Max Depth = 5 and Max Depth = 7) achieved near-perfect accuracy (~99.98% and ~99.99%, respectively), highlighting the capacity to capture intricate patterns at the cost of interpretability.

        **Role of Tree Depth**:  
        - **Max Depth = 3**: Provided a simple, interpretable tree structure but with limited granularity, resulting in a few misclassifications.  
        - **Max Depth = 5**: Achieved a balance between complexity and classification performance, minimizing misclassifications while remaining interpretable.  
        - **Max Depth = 7**: Maintained high accuracy but introduced additional complexity, which did not yield further performance gains and increased risk of overfitting.

        **Classification Insights**:  
        - The Decision Tree models effectively distinguished between Low, Medium, and High air quality categories.  
        - Deeper trees helped resolve misclassifications observed with shallow trees, highlighting the need for depth tuning to achieve optimal results.
        """)

        st.markdown("##### 2. Predictive Applications")
        st.write("""
        The predictive capabilities of the Decision Tree models provide several real-world applications:

        **Environmental Monitoring**:  
        - The model can be used to predict air quality in real-time, allowing for proactive interventions and public health advisories.  
        - This predictive capability can be used to identify regions with poor air quality and guide targeted mitigation measures.

        **Policy and Regulatory Decision-Making**:  
        - Insights into key pollutant predictors can inform the development of regulatory policies aimed at reducing specific pollutant levels such as `pm25` and `pm10`.

        **Urban Planning and Public Health Initiatives**:  
        - Understanding the factors influencing air pollution enables strategic planning to minimize exposure through initiatives such as green zones, optimized traffic flows, and pollution control strategies.
        """)

        st.markdown("##### 3. Limitations")
        st.write("""
        Despite the high accuracy and valuable insights provided by the Decision Tree models, some limitations were observed:

        **Model Overfitting**:  
        - Increasing the depth beyond a certain level did not yield significant improvements, indicating a risk of overfitting and necessitating careful model complexity management.

        **Feature Engineering**:  
        - The performance of the models relied solely on available pollutant features. Incorporating additional features such as weather patterns or urban activity data could improve predictive accuracy.

        **Scalability**:  
        - With larger datasets or more complex feature sets, Decision Trees may become less interpretable and computationally intensive, necessitating further optimization techniques.
        """)

        st.markdown("##### 4. Future Work")
        st.write("""
        To enhance the findings of this analysis, several future directions are recommended:

        **Testing Ensemble Methods**:  
        - Employing ensemble techniques like Random Forests and Gradient Boosting to improve classification accuracy and minimize overfitting risks.

        **Incorporating Additional Features**:  
        - Integrating external data such as meteorological conditions, industrial activities, or urban density to enrich predictive capabilities.

        **Exploring Non-linear Relationships**:  
        - Using feature transformations or interaction terms to capture more complex patterns.

        **Cross-Validation and External Validation**:  
        - Testing on unseen datasets to assess model robustness and generalizability.
        """)

        st.markdown("##### 5. Final Thoughts")
        st.write("""
        The Decision Tree models highlighted the critical role of pollutants like `pm25` and `pm10` in predicting air quality levels. Balancing model depth is crucial to ensure accurate predictions without overfitting. This data-driven approach has the potential to inform policies, guide public health measures, and enhance environmental monitoring strategies for air quality improvement.
        """)

    elif sub_tab == "Regression":
        st.write("#### Overview")
        st.markdown("### Linear Regression")
        st.write("""
        Linear regression is a statistical approach used to model the relationship between a dependent variable (target) and one or more independent variables (predictors) by fitting a linear equation to the observed data. The equation takes the form: **y = β0 + β1x1 + β2x2 + ... + βnxn + ε**, where **y** is the predicted output, **β0** is the intercept, **β1, β2, ..., βn** are coefficients, **x1, x2, ..., xn** are input features, and **ε** represents the error term. Linear regression aims to minimize the sum of squared residuals (differences between observed and predicted values). It is widely used in predictive modeling and forecasting.
        """)

        # Logistic Regression
        st.markdown("### Logistic Regression")
        st.write("""
        Logistic regression is used for modeling binary outcomes (e.g., 0/1, Yes/No). Unlike linear regression, it predicts the probability that an instance belongs to a specific class. It uses the **sigmoid function**, defined as **f(x) = 1 / (1 + e^(-z))**, to map predictions to probabilities between 0 and 1. Here, **z** is the linear combination of input features and their weights (similar to linear regression). Logistic regression finds application in classification tasks, such as determining whether an email is spam or predicting disease presence.
        """)
        st.image("Images/Reg1.jpg", caption="Linear and Logistic Regression")

        # Similarities and Differences
        st.markdown("### Similarities and Differences Between Linear and Logistic Regression")
        st.write("""
        Linear and logistic regression both examine relationships between dependent and independent variables. However, linear regression predicts continuous values, whereas logistic regression predicts probabilities for categorical outcomes. Linear regression minimizes residual error using ordinary least squares, while logistic regression employs maximum likelihood estimation to optimize the fit of log-odds. Linear regression models data using a straight line, while logistic regression uses a sigmoid curve to represent probabilities for binary classification.
        """)

        # Use of Sigmoid Function
        st.markdown("### Use of Sigmoid Function in Logistic Regression")
        st.write("""
        Logistic regression uses the sigmoid function to map predicted values to probabilities between 0 and 1. The sigmoid function transforms linear predictions into a probability distribution, making it suitable for binary classification problems. Mathematically, the sigmoid function is represented as **f(x) = 1 / (1 + e^(-x))**. This transformation allows logistic regression to output probabilities, making it ideal for applications where a probabilistic interpretation of class membership is required.
        """)

        # Maximum Likelihood Estimation
        st.markdown("### Maximum Likelihood Estimation in Logistic Regression")
        st.write("""
        Maximum likelihood estimation (MLE) is a technique used in logistic regression to find the best-fitting parameters for the model. It aims to maximize the likelihood function, which represents the probability of the observed data given a set of parameters. By iteratively adjusting coefficients, MLE seeks to find the parameter values that make the observed data most probable. This approach ensures that the logistic regression model accurately predicts class probabilities for the given data.
        """)

        st.write("#### Data Preparation")
    
        st.write("""
Proper data preparation is essential for building effective regression models. Since regression is a supervised learning method, it requires labeled data, where each instance in the dataset is associated with a known target or output variable. The data preparation process involves cleaning and preprocessing data, handling missing values, encoding categorical variables if needed, and normalizing or scaling features. The data is then split into training and testing sets to ensure unbiased evaluation of the model's performance. This preparation is crucial for accurate predictions, as it enables the regression model to learn relationships between the input features and the target variable in a meaningful way.
""")
        
        image_path_original = "Images/15.png" 
        st.image(image_path_original, use_column_width=True, caption="Original Dataset")

        st.write("""
        - The dataset was transformed using `.pivot_table()` to reorganize pollutants as separate columns. This facilitated the analysis by clearly structuring pollutant values against unique locations and timestamps.
        - Essential columns, including pollutant values (`pm25`, `pm10`, `no2`, `so2`, `o3`, `co`), were retained, and rows with missing data were removed to ensure data integrity.
        - Columns such as `latitude` and `longitude` were excluded to streamline the dataset for pollutant-focused analysis.
        - The dataframe index was reset to maintain a clean and sequential structure, simplifying subsequent data handling.
    """)

        st.image("Images/Naive4.png", caption="Dataset after Cleaning", use_column_width=True)
        st.write("""
    To prepare the dataset for binary classification of air quality levels, median values of the `pm25` and `pm10` pollutants were calculated as thresholds. This step enables segmentation into 'high' and 'low' air quality categories, facilitating binary classification modeling.

    **Steps Taken**:
    
    - **Threshold Calculation**: The median values for `pm25` and `pm10` were computed to serve as reference points. These medians act as the thresholds to categorize air quality into two classes.
    
    - **Binary Categorization**: A function was created to assign a binary label to each row in the dataset. If both `pm25` and `pm10` values exceed their median thresholds, the air quality is labeled as '1' (high). Otherwise, it is labeled as '0' (low).
    
    - **Class Distribution Check**: The distribution of the newly created binary target variable, `air_quality_binary`, provides insights into the balance of high and low air quality samples. This is essential for ensuring that subsequent models are appropriately trained and evaluated.
""")
        st.image("Images/Reg2.png", caption="Distribution of Air Quality Binary Classes")

        st.write("""The dataset now looks like this:""")
        st.image("Images/Reg3.png", caption="Prepared Dataset", use_column_width=True)

        st.write("""Features:""")
        st.image("Images/Reg4.png", caption="Features", use_column_width=True)

        st.write("""Target Variable:""")
        st.image("Images/Reg5.png", caption="Target", use_column_width=True)

        st.write("""
    Before applying logistic regression, it is important to standardize the features to ensure that they have a mean of 0 and a standard deviation of 1. This 
    step is particularly crucial for models like logistic regression that use optimization algorithms sensitive to feature scaling. Standardization helps in 
    faster convergence of the algorithm and prevents features with larger magnitudes from dominating those with smaller values.

    The `StandardScaler` from `sklearn.preprocessing` was used to transform all feature values to a standardized scale.

    Next, the dataset was divided into training and testing subsets using a 70-30 split ratio. The training set (70%) was used to train the logistic regression 
    model, while the testing set (30%) was reserved for evaluating its performance. This ensures that the model's accuracy and generalization capabilities are 
    assessed on data that it has not previously encountered.
""")
    
        st.image("Images/Reg6.png", caption="X_train Dataset", use_column_width=True)
        st.image("Images/Reg7.png", caption="X_test Dataset", use_column_width=True)
        st.image("Images/Reg8.png", caption="y_train Dataset", use_column_width=True)
        st.image("Images/Reg9.png", caption="y_test Dataset", use_column_width=True)

        st.write("#### Importance of Creating a Disjoint Split")

        st.write("""
        ##### Prevention of Overfitting
        Models trained on data learn specific patterns and relationships from the training dataset. If the same data is used for both training and evaluation, performance metrics can appear artificially inflated due to the model's prior exposure to the data. This situation, referred to as **data leakage**, results in overfitting, where the model may perform exceptionally well on known data but exhibit poor generalization on unseen data. A disjoint split ensures that evaluation occurs on data that has not been seen during training, thus providing an unbiased assessment of model performance and reducing overfitting risk.

        ##### Assessment of Generalization Capability
        Machine learning models must generalize effectively to new and previously unseen data. Using a disjoint test set simulates real-world scenarios where models are deployed to predict or classify novel inputs. For the air quality dataset, this approach enables a robust evaluation of the model's predictive ability on new pollutant measurements, including `pm25`, `pm10`, and other features.

        ##### Validation of Model Robustness
        When models are trained and evaluated on overlapping data, there is a risk that unique characteristics or outliers in the training data may be memorized. This behavior compromises the model's robustness and reliability. Ensuring a disjoint split allows the test set to serve as an unbiased benchmark for evaluating the model's predictions, confirming that predictions are driven by learned patterns rather than noise or specific training artifacts.
        """)

        # Link to code and data
        st.markdown("#### Code and Data")
        st.markdown("[Code](https://github.com/starlord-31/Global-Air-Quality-Analysis/blob/main/Regression.ipynb)")
        st.markdown("[Data](https://drive.google.com/drive/folders/1yNMIIAGMYQi_tx_nimV0yBb09Kpmt66K?usp=drive_link)")

        st.write("#### Results")
        st.image("Images/Reg10.png", caption="Accuracy and Confusion Matrices", use_column_width=True)
        st.write("""
    #### Logistic Regression Results
    The Logistic Regression model was applied to predict binary air quality categories using various features. This approach models a linear decision boundary 
    and uses the logistic (sigmoid) function to estimate class probabilities.

    **Accuracy**: 93.24%  
    The high accuracy demonstrates the model's ability to classify most instances correctly, suggesting a strong fit with minimal misclassifications.

    **Confusion Matrix**:
    - **True Positives (TP)**: The model correctly classified 10,346 instances of Class 0 (low air quality).
    - **True Negatives (TN)**: It accurately predicted 6,253 instances of Class 1 (high air quality).
    - **False Positives (FP)**: There were 522 instances incorrectly classified as Class 1 when they actually belonged to Class 0.
    - **False Negatives (FN)**: 681 instances were predicted as Class 0 when they truly belonged to Class 1.
    This indicates a small amount of misclassification, demonstrating high precision and recall, especially for Class 1 predictions.""")
        
        st.write("""
    #### Multinomial Naive Bayes Results
    Multinomial Naive Bayes (MNB) was used as a comparative model for classifying air quality categories. Given MNB's assumption of non-negative values, the data 
    was adjusted accordingly.

    **Accuracy**: 86.43%  
    This accuracy is somewhat lower than Logistic Regression, reflecting its limitations given the data's distribution. However, it remains a valid approach for 
    classification.

    **Confusion Matrix**:  
    - **TP**: 10,005 instances of Class 0 were correctly identified.
    - **TN**: The model correctly predicted 5,382 instances of Class 1.
    - **FP**: 863 instances were incorrectly classified as Class 1 instead of Class 0.
    - **FN**: 1,552 instances were predicted as Class 0 instead of being correctly identified as Class 1.
    The higher number of false negatives and false positives suggests that this model struggles more with correctly differentiating between the two classes compared to Logistic Regression, potentially due to data distribution characteristics that do not align as well with Naive Bayes' assumptions.""")
        st.image("Images/Reg12.png", caption="Confusion Matrices", use_column_width=True)
        st.write("""In comparison, Logistic Regression demonstrates better overall performance than Multinomial Naive Bayes for this dataset. This can be attributed to the 
    linear separation characteristics and data distribution, highlighting Logistic Regression's suitability for the given features.
""")
        st.write("""
    ### Model Accuracy Comparison
    This bar chart compares the accuracy of Logistic Regression and Multinomial Naive Bayes models on the air quality prediction task. 

    - **Logistic Regression** achieved a higher accuracy of 93.24%, indicating its strong performance and suitability for this dataset.
    - **Multinomial Naive Bayes** achieved an accuracy of 86.43%, showing good predictive capabilities but falling slightly behind Logistic Regression.

    The difference in accuracies highlights the strengths of Logistic Regression in handling this particular dataset, possibly due to its linear decision boundary and handling of feature distributions, whereas the assumptions of Multinomial Naive Bayes may have been less aligned with the data characteristics.
""")
        st.image("Images/Reg11.png", caption="Accuracy Comparison Between Logistic Regression and Multinomial Naive Bayes Models")

        st.write("""
    ### ROC Curve Comparison
    The Receiver Operating Characteristic (ROC) curve illustrates the performance of the Logistic Regression and Multinomial Naive Bayes models by comparing 
    the True Positive Rate (TPR) against the False Positive Rate (FPR) at various threshold levels.

    **Logistic Regression** achieved an Area Under the Curve (AUC) of 0.99, indicating a very strong ability to distinguish between the classes. The curve 
    rises quickly towards the top left, reflecting high sensitivity and low false positive rates.

    **Multinomial Naive Bayes** achieved an AUC of 0.87, demonstrating good performance, though not as strong as Logistic Regression. This suggests that 
    while MNB can classify effectively, it does so with slightly more overlap between classes compared to Logistic Regression.

    The diagonal dashed line represents a random guess baseline (AUC = 0.5). Both models outperform this baseline, indicating their effectiveness in predicting 
    the target variable.
""")
        st.image("Images/Reg13.png", caption="ROC Curve Comparison Between Logistic Regression and Multinomial Naive Bayes Models")

        st.write("""
    #### Conclusion and Key Learnings

    1. **Model Performance Insights**:
       - Logistic Regression demonstrated a strong ability to distinguish between air quality categories, achieving a high accuracy of 93.24%. This model 
         efficiently utilized linear decision boundaries to separate classes, as reflected by its strong performance metrics and high Area Under the Curve (AUC) 
         score of 0.99. This suggests that a linear relationship between features and classes is well captured by this model.
       - Multinomial Naive Bayes, while achieving a respectable accuracy of 86.43%, did not perform as well as Logistic Regression. Its performance was hindered 
         by overlapping feature distributions and assumptions regarding non-negative input values. Nonetheless, it demonstrated a solid ability to categorize air 
         quality, reflected by its AUC score of 0.87.

    2. **Classification Insights**:
       - The results from Logistic Regression indicate that the data's linear separability plays a significant role in accurate classification. The low rate of 
         false positives and false negatives further highlights the model's effectiveness in discriminating between air quality categories.
       - The performance of Multinomial Naive Bayes, although lower, reveals useful patterns in the data. It particularly struggled with misclassifying instances 
         near decision boundaries, suggesting that additional feature transformations or non-linear modeling approaches may yield better results.

    3. **Predictive Applications**:
       - Logistic Regression's robust performance implies that it can be effectively used for predicting air quality levels in practical scenarios, providing 
         reliable probability estimates for each class.
       - Multinomial Naive Bayes, due to its efficiency with text-like and discrete data, offers value for applications requiring simpler probabilistic outputs 
         despite some classification limitations in this context.

    4. **Future Improvements**:
       - Exploring feature engineering techniques or interaction terms may further enhance model performance.
       - Testing other classification models or ensemble techniques could address limitations in distinguishing overlapping class distributions.
""")

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
