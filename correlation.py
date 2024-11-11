#positive correlation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
np.random.seed(1)
x=np.random.randint(0,50,1000)
y=x+np.random.normal(0,10,1000)
np.corrcoef(x,y)
matplotlib.style.use('ggplot')
plt.scatter(x,y)
plt.show()

#negative correlation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
np.random.seed(1)
x=np.random.randint(0,50,1000)
y=100 - x + np.random.normal(0,50,1000)
np.corrcoef(x,y)
matplotlib.style.use('ggplot')
plt.scatter(x,y)
plt.show()

#no/weak correlation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
np.random.seed(1)
x=np.random.randint(0,50,1000)
y=np.random.randint(0,50,1000)
np.corrcoef(x,y)
plt.scatter(x,y)
plt.show()



