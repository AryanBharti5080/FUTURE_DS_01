# Retail Sales Analytics Report

## 1. Executive Summary

This report presents an analysis of retail sales data from the Superstore dataset. The project uses transaction-level sales records to understand overall business performance, profitability, customer segments, product categories, regions, shipping modes, and discount impact.

The business generated total sales of **2,297,200.86** and total profit of **286,397.02** from **9,994** records between **2014-01-03** and **2017-12-30**. Sales and profit improved over the years, with 2017 recording the highest sales and profit. However, profitability is uneven across product sub-categories and states. High discounts, especially above 40%, are strongly associated with losses.

## 2. Project Objective

The objective of this project is to analyze retail sales performance and create a Power BI dashboard that helps users identify:

- Overall sales and profit performance
- Sales trends over time
- Regional and state-level performance
- Category and sub-category profitability
- Customer segment contribution
- Discount-related profit loss
- Areas requiring business improvement

## 3. Dataset Overview

The dataset used for this project is:

```text
Dataset/superstore_sales.csv
```

### Dataset Summary

| Metric | Value |
| --- | ---: |
| Total Rows | 9,994 |
| Total Orders | 5,009 |
| Total Customers | 793 |
| Total Products | 1,862 |
| Total Sales | 2,297,200.86 |
| Total Profit | 286,397.02 |
| Total Quantity Sold | 37,873 |
| Date Range | 2014-01-03 to 2017-12-30 |

### Important Fields

| Field | Description |
| --- | --- |
| Order Date | Date when the order was placed |
| Ship Date | Date when the order was shipped |
| Ship Mode | Shipping class selected by the customer |
| Segment | Customer segment such as Consumer, Corporate, or Home Office |
| Region | Sales region |
| State / City | Geographic sales location |
| Category | Main product category |
| Sub-Category | Product sub-category |
| Sales | Revenue generated |
| Quantity | Number of units sold |
| Discount | Discount applied on the order |
| Profit | Profit or loss from the order |

## 4. Key Performance Indicators

| KPI | Value |
| --- | ---: |
| Total Sales | 2,297,200.86 |
| Total Profit | 286,397.02 |
| Total Quantity | 37,873 |
| Total Orders | 5,009 |
| Total Customers | 793 |
| Profit Margin | 12.47% |

## 5. Yearly Performance

| Year | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| 2014 | 484,247.50 | 49,543.97 | 7,581 |
| 2015 | 470,532.51 | 61,618.60 | 7,979 |
| 2016 | 609,205.60 | 81,795.17 | 9,837 |
| 2017 | 733,215.26 | 93,439.27 | 12,476 |

### Observation

Sales dipped slightly in 2015 compared to 2014, but profit still increased. From 2016 onward, both sales and profit grew strongly. The best-performing year was 2017, with the highest sales, profit, and quantity sold.

## 6. Regional Performance

| Region | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| West | 725,457.82 | 108,418.45 | 12,266 |
| East | 678,781.24 | 91,522.78 | 10,618 |
| Central | 501,239.89 | 39,706.36 | 8,780 |
| South | 391,721.91 | 46,749.43 | 6,209 |

### Observation

The West region generated the highest sales and profit. The East region also performed strongly. The Central region generated higher sales than the South but earned lower profit, which suggests margin pressure or loss-making product mixes in that region.

## 7. Category Performance

| Category | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| Technology | 836,154.03 | 145,454.95 | 6,939 |
| Furniture | 741,999.80 | 18,451.27 | 8,028 |
| Office Supplies | 719,047.03 | 122,490.80 | 22,906 |

### Observation

Technology generated the highest sales and profit. Office Supplies had the highest quantity sold and strong profit contribution. Furniture generated high sales but very low profit compared to the other categories, making it a key area for further review.

## 8. Sub-Category Performance

### Most Profitable Sub-Categories

| Sub-Category | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| Copiers | 149,528.03 | 55,617.82 | 234 |
| Phones | 330,007.05 | 44,515.73 | 3,289 |
| Accessories | 167,380.32 | 41,936.64 | 2,976 |
| Paper | 78,479.21 | 34,053.57 | 5,178 |
| Binders | 203,412.73 | 30,221.76 | 5,974 |

### Least Profitable Sub-Categories

| Sub-Category | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| Tables | 206,965.53 | -17,725.48 | 1,241 |
| Bookcases | 114,880.00 | -3,472.56 | 868 |
| Supplies | 46,673.54 | -1,189.10 | 647 |
| Fasteners | 3,024.28 | 949.52 | 914 |
| Machines | 189,238.63 | 3,384.76 | 440 |

### Observation

Copiers, Phones, and Accessories are major profit contributors. Tables, Bookcases, and Supplies are loss-making sub-categories. Tables are especially concerning because they generated high sales but produced the largest loss.

## 9. Segment Performance

| Segment | Sales | Profit | Quantity |
| --- | ---: | ---: | ---: |
| Consumer | 1,161,401.34 | 134,119.21 | 19,521 |
| Corporate | 706,146.37 | 91,979.13 | 11,608 |
| Home Office | 429,653.15 | 60,298.68 | 6,744 |

### Observation

The Consumer segment is the largest contributor to sales, profit, and quantity. Corporate and Home Office segments are smaller but still profitable. Marketing and retention strategies should prioritize Consumer customers while also looking for growth opportunities in Corporate accounts.

## 10. State-Level Performance

### Top Profitable States

| State | Sales | Profit |
| --- | ---: | ---: |
| California | 457,687.63 | 76,381.39 |
| New York | 310,876.27 | 74,038.55 |
| Washington | 138,641.27 | 33,402.65 |
| Michigan | 76,269.61 | 24,463.19 |
| Virginia | 70,636.72 | 18,597.95 |

### Loss-Making States

| State | Sales | Profit |
| --- | ---: | ---: |
| Texas | 170,188.05 | -25,729.36 |
| Ohio | 78,258.14 | -16,971.38 |
| Pennsylvania | 116,511.91 | -15,559.96 |
| Illinois | 80,166.10 | -12,607.89 |
| North Carolina | 55,603.16 | -7,490.91 |

### Observation

California and New York are the strongest profit contributors. Texas, Ohio, Pennsylvania, and Illinois are major loss areas. These states should be reviewed for discounting patterns, shipping costs, product mix, and pricing strategy.

## 11. Shipping Mode Performance

| Ship Mode | Sales | Profit | Quantity | Rows |
| --- | ---: | ---: | ---: | ---: |
| Standard Class | 1,358,215.74 | 164,088.79 | 22,797 | 5,968 |
| Second Class | 459,193.57 | 57,446.64 | 7,423 | 1,945 |
| First Class | 351,428.42 | 48,969.84 | 5,693 | 1,538 |
| Same Day | 128,363.12 | 15,891.76 | 1,960 | 543 |

### Observation

Standard Class is the most used and highest contributing shipping mode. Same Day shipping has the lowest sales and profit, but it remains profitable in the dataset.

## 12. Discount Impact

| Discount Bucket | Sales | Profit | Rows |
| --- | ---: | ---: | ---: |
| 0% | 1,087,908.47 | 320,987.60 | 4,798 |
| 1-20% | 846,522.24 | 100,785.47 | 3,803 |
| 21-40% | 234,137.90 | -35,817.47 | 460 |
| Over 40% | 128,632.25 | -99,558.59 | 933 |

### Observation

Orders with no discount and low discounts are profitable. Discounts above 20% lead to losses, and discounts above 40% create the largest negative impact. Discount control is one of the most important improvement opportunities in this project.

## 13. Key Findings

- Total sales were **2,297,200.86**, with profit of **286,397.02**.
- The business achieved an overall profit margin of approximately **12.47%**.
- Sales and profit grew strongly in 2016 and 2017.
- The **West** region had the highest sales and profit.
- **Technology** was the most profitable category.
- **Furniture** had high sales but weak profit.
- **Tables**, **Bookcases**, and **Supplies** were loss-making sub-categories.
- **Consumer** was the largest and most profitable customer segment.
- **California** and **New York** were the strongest states by profit.
- **Texas**, **Ohio**, **Pennsylvania**, and **Illinois** produced major losses.
- Discounts above **20%** were associated with negative profit.

## 14. Recommendations

1. Reduce or control high discounting, especially discounts above 20%.
2. Review pricing, supplier cost, and discount strategy for Tables and Bookcases.
3. Investigate loss-making states such as Texas, Ohio, Pennsylvania, and Illinois.
4. Increase focus on profitable product areas such as Copiers, Phones, Accessories, and Paper.
5. Continue strengthening the West and East regions because they generate high profit.
6. Improve Furniture category profitability through better pricing and product mix decisions.
7. Use customer segmentation to design targeted campaigns for Consumer and Corporate customers.
8. Monitor yearly trends to maintain the growth achieved in 2016 and 2017.

## 15. Conclusion

The retail sales analysis shows that the business is growing and profitable overall, but profitability is not evenly distributed. Strong performance comes from Technology, Office Supplies, the West region, and states such as California and New York. At the same time, losses from high discounts, Furniture sub-categories, and certain states reduce overall profit.

The Power BI dashboard created for this project can help decision-makers monitor these patterns and take action on discounting, product strategy, and regional performance.

