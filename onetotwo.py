#part one
import numpy as np
annual_mortality_all=18/1000
annual_death_stroke = 36.2/100000
non_stroke_mortality=(18*100-36.2)/100000

rate_stroke= -np.log(1 - annual_death_stroke)
rate_non_stroke= -np.log(1-non_stroke_mortality)
print('the rate of stoke associated mortality events is', rate_stroke)
print('the rate of non-stoke associated mortality events is', rate_non_stroke)

#part two
annual_mortality_first_stroke=15/1000
annual_stroke_rate=-np.log(1-annual_mortality_first_stroke)
print('the annual rate of stroke for our population is', annual_stroke_rate)

#part three
lambda1=annual_stroke_rate*.9
lambda2=annual_stroke_rate*.1
print('annual rate of transition from well to stroke is', lambda1)
print('annual rate of transition from well to death is', lambda2)

#part four
recurrent_stroke=0.17
annual_recurret_stroke=-np.log(1-recurrent_stroke)/5
print('annual rate of recurrent stroke is', annual_recurret_stroke)

#part five
lambda3=annual_recurret_stroke*0.8
lambda4=annual_recurret_stroke*0.2
print('annual rate of transition from poststroke to stroke is', lambda3)
print('annual rate of transition from poststroke to death is', lambda4)

#part six
average_survival_rate=7/365
annual_rate_stroke_pstroke=1/average_survival_rate
print('the annual rate of transition from stroke to poststroke is', annual_rate_stroke_pstroke)


#problem two
rate_stroke_pstroke_use=annual_rate_stroke_pstroke*0.75
therapy_non_stroke_deathrate=rate_non_stroke*1.05


