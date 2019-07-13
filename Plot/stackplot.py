#%%
import matplotlib.pyplot as plt
hours = [1,2,3,4,5]

planning =[7,8,6,11,7]
design = [2,3,4,3,2]
code = [7,8,7,2,2]
review = [8,5,7,8,13]

plt.plot([],[],color='yellow', label='planning', linewidth=5)
plt.plot([],[],color='orange', label='design', linewidth=5)
plt.plot([],[],color='green', label='code', linewidth=5)
plt.plot([],[],color='black', label='review', linewidth=5)

plt.stackplot(hours,planning,design,code,review, colors=['yellow','orange','green','black'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Stack Plot -- Quppler')
plt.legend()
plt.show()

#%%
