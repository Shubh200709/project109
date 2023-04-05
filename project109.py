import pandas as pd
import statistics

#reading data
frame = pd.read_csv('StudentsPerformance.csv')

#initialising dataframes
mathscore = frame['math score'].to_list()
readingscore = frame['reading score'].to_list()
writingscore = frame['writing score'].to_list()

#finding mean, median, mode and stdev of math score
mathscore_mean = statistics.mean(mathscore)
mathscore_median = statistics.median(mathscore)
mathscore_mode = statistics.mode(mathscore)
mathscore_stdev = statistics.stdev(mathscore)

#finding mean, median, mode, stdev of reading score
readingscore_mean = statistics.mean(readingscore)
readingscore_median = statistics.median(readingscore)
readingscore_mode = statistics.mode(readingscore)
readingscore_stdev = statistics.stdev(readingscore)

#finding mean, median, mode, stdev of writing score
writingscore_mean = statistics.mean(writingscore)
writingscore_median = statistics.median(writingscore)
writingscore_mode = statistics.mode(writingscore)
writingscore_stdev = statistics.stdev(writingscore)

#start and end
math_loop_start_1, math_loop_end_1 = mathscore_mean - mathscore_stdev, mathscore_mean + mathscore_stdev
math_loop_start_2, math_loop_end_2 = mathscore_mean - (2*mathscore_stdev), mathscore_mean + (2*mathscore_stdev)
math_loop_start_3, math_loop_end_3 = mathscore_mean - (3*mathscore_stdev), mathscore_mean + (3*mathscore_stdev)

reading_loop_start_1, reading_loop_end_1 = readingscore_mean - readingscore_stdev, readingscore_mean + readingscore_stdev
reading_loop_start_2, reading_loop_end_2 = readingscore_mean - (2*readingscore_stdev), readingscore_mean + (2*readingscore_stdev)
reading_loop_start_3, reading_loop_end_3 = readingscore_mean - (3*readingscore_stdev), readingscore_mean + (3*readingscore_stdev)

writing_loop_start_1, writing_loop_end_1 = writingscore_mean - writingscore_stdev, writingscore_mean + writingscore_stdev
writing_loop_start_2, writing_loop_end_2 = writingscore_mean - (2*writingscore_stdev), writingscore_mean + (2*writingscore_stdev)
writing_loop_start_3, writing_loop_end_3 = writingscore_mean - (3*writingscore_stdev), writingscore_mean + (3*writingscore_stdev)

#data sorting
sort_math_1 = [i for i in mathscore if i > math_loop_start_1 and i < math_loop_end_1]
sort_math_2 = [i for i in mathscore if i > math_loop_start_2 and i < math_loop_end_2]
sort_math_3 = [i for i in mathscore if i > math_loop_start_3 and i < math_loop_end_3]

sort_reading_1 = [i for i in readingscore if i > reading_loop_start_1 and i < reading_loop_end_1]
sort_reading_2 = [i for i in readingscore if i > reading_loop_start_2 and i < reading_loop_end_2]
sort_reading_3 = [i for i in readingscore if i > reading_loop_start_3 and i < reading_loop_end_3]

sort_writing_1 = [i for i in writingscore if i > writing_loop_start_1 and i < writing_loop_end_1]
sort_writing_2 = [i for i in writingscore if i > writing_loop_start_2 and i < writing_loop_end_2]
sort_writing_3 = [i for i in writingscore if i > writing_loop_start_3 and i < writing_loop_end_3]

#percentage
print("{}% of data in mathscore lies in the 1st standard deviation".format((len(sort_math_1)/len(mathscore))*100.0))
print("{}% of data in mathscore lies in the 2nd standard deviation".format((len(sort_math_2)/len(mathscore))*100.0))
print("{}% of data in mathscore lies in the 3rd standard deviation".format((len(sort_math_3)/len(mathscore))*100.0))

print(" ")

print("{}% of data in readingscore lies in the 1st standard deviation".format((len(sort_reading_1)/len(readingscore))*100.0))
print("{}% of data in readingscore lies in the 2nd standard deviation".format((len(sort_reading_2)/len(readingscore))*100.0))
print("{}% of data in readingscore lies in the 3rd standard deviation".format((len(sort_reading_3)/len(readingscore))*100.0))

print(" ")

print("{}% of data in writingscore lies in the 1st standard deviation".format((len(sort_writing_1)/len(writingscore))*100.0))
print("{}% of data in writingscore lies in the 2nd standard deviation".format((len(sort_writing_2)/len(writingscore))*100.0))
print("{}% of data in writingscore lies in the 3rd standard deviation".format((len(sort_writing_3)/len(writingscore))*100.0))
