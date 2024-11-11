import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
data = {'Factor_A': ['A1','A1','A1','A1','A2','A2','A2','A2'],
        'Factor_B': ['B1','B1','B2','B2','B1','B1','B2','B2'],
        'Response': [5,6,7,8,6,7,8,9]
        }
df = pd.DataFrame(data)
model = ols('Response ~ C(Factor_A) + C(Factor_B) + C(Factor_A):C(Factor_B)',data=df).fit()
anova_results = anova_lm(model)
print(anova_results)
