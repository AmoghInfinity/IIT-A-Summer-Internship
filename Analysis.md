From Statistics Summary we can conclude the following points:
Used Car Age- The data covers a wide range (1996-2019), indicating a mix of recent and older models to fit various buyer preferences.
Mileage Analysis- The average mileage of 58,000 kilometers provides a baseline for typical car usage. However, a suspected outlier with an extremely high value (650,000 km) might be skewing the data. This record might need removal for a more accurate analysis. Additionally, cars with 0 kilometers likely represent data entry errors and should be investigated.
Engine and Power Distribution- The data for engine and power specifications might contain outliers and show a rightward skew. This could be because the dataset includes a variety of car types, with smaller engines in sedans and larger engines in SUVs.
Focus on Seats- The average of 5 seats suggests a prevalence of sedans or smaller SUVs. As you rightly pointed out, the number of seats can significantly impact the price, with cars offering more seating potentially commanding higher prices, especially minivans and large SUVs.
Questionable Maximum Price- The highest listed price of 160,000 (currency unspecified) seems unusually high compared to other listings and could be an outlier or a data entry error. This data point deserves further examination
From Count PLot we get the following information:
Inventory Hotspot- Mumbai boasts the most extensive selection of used cars for sale, followed by Hyderabad and Coimbatore.
Dominant Diesel- Diesel reigns supreme as the fuel type for nearly 53% of the cars, possibly due to its association with better performance.
Manual Gear Shift Reigns- The majority (72%) of cars come with manual transmissions, suggesting a preference for this style in the used car market.
First-Hand Preference- A strong preference for first-owner cars is evident, with a whopping 82% falling into this category. This suggests buyers prioritize vehicles with a single previous owner.
Brand Leaders- Maruti takes the crown as the most popular brand, accounting for 20% of the cars. Hyundai follows closely behind with a 19% share.
WagonR Tops the Charts- The WagonR emerges as the single most prevalent model available for purchase.
Since Kilometers driven and Price variables were highly skewed and were on a larger scale we did a log transform on those variables. This helped in normalisation and the variables can maintain a standard scale with other variables.
Pair Plot gives the following insights:
Newer Cars Cost More, But Have Lower Mileage- There's a positive correlation between the car's year (newer model) and its price. This makes sense as newer cars tend to be pricier. However, newer cars also tend to have lower mileage readings since they haven't been driven for as long.
Older Cars Have Higher Mileage- Conversely, there's a negative correlation between the car's year (older model) and the kilometers driven. This means older cars typically have accumulated more mileage over time.
Less Mileage Often Means More Power (but Lower Fuel Economy)- Mileage and power tend to have a negative correlation. Cars with lower mileage (driven less) often have higher engine power ratings. However, this can also come at the cost of lower fuel efficiency, meaning they might use more gas.
Price Drops As Cars Age- The price of a car generally decreases as the year (and age) increases. This is because newer models offer advancements and depreciate less quickly.
Bigger Engines and More Power Mean Higher Prices- Engine size and power tend to be positively correlated with price. Cars boasting larger engines and higher horsepower ratings typically come with a steeper price tag.
EDA Bivariate Ananlysis Observation:
Geographic Price Variations- Cars tend to be pricier in Coimbatore compared to Kolkata and Jaipur. This could be due to factors like local demand, availability of certain car models, or even taxes.
Automatic Transmission Premium- Cars with automatic transmissions generally command a higher price than those with manual transmissions. This reflects the added convenience and potentially higher demand for automatics.
Fuel Efficiency Matters- Diesel and electric cars, often associated with better fuel efficiency, are found to be the most expensive options. LPG cars, on the other hand, are typically the most affordable due to lower fuel costs.
Ownership History Affects Price: First-owner cars tend to be priced higher than those with more owners. Buyers often place a premium on vehicles with a single previous owner, potentially indicating better care and maintenance. The price dips further for third-owner cars compared to those with four or more owners, suggesting a declining value with each ownership change.
Luxury Brand Supremacy- The Lamborghini brand reigns supreme in terms of price, reflecting its association with luxury and exclusivity.
Price and Seating Capacity- Cars with two seats, often high-performance sports cars, carry the highest price tag. This is likely due to a combination of factors like powerful engines, luxurious materials, and a niche market appeal. Conversely, 7-seater cars, typically associated with family needs, tend to be offered at a lower price point.
New Cars Command a Premium- As expected, the latest model cars come with a higher price compared to older models. This reflects advancements in technology, safety features, and overall desirability.
