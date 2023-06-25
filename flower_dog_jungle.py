#Entrepreneurship Training Program

#import statements
import sys
import math
import datetime

#defining a funtion
def entrepreneurship_training_program(training_duration, course_details):
  """
  This function is responsible for running an entrepreneurship training program.

  Arguments:
    training_duration (int): The number of weeks the course will last.
    course_details (dict): Contains the details of the course such as the topics to be covered and any prerequisites.

  Returns:
    None
  """  
  #Initialization
  final_grade = 0
  training_start_date = datetime.datetime.now()
  training_end_date = training_start_date + datetime.timedelta(weeks = training_duration)

  #Looping over the course details
  for topic, prerequisites in course_details.items():
    #Checking for any prerequisites
    if prerequisites:
      #Looping over the prerequisites
      for prerequisite in prerequisites:
        print('Please complete {} before starting the course on {}'.format(prerequisite, topic))
     
    #Calculating final grade
    final_grade += math.ceil(training_duration/len(course_details))
  
  #Printing summary
  print('Training will start on {} and end on {}'.format(training_start_date.strftime('%d %B %Y'), 
                                                        training_end_date.strftime('%d %B %Y')))
  print('You will be given a grade of {} upon completion of the course.'.format(final_grade))
  
#Main Function
if __name__ == '__main__':
  training_duration = int(sys.argv[1])
  course_details = {
    'Fundamentals of Entrepreneurship': ['Micro- and Macro-Economics'],
    'BusinessPlanning': ['Accounting Basics'],
    'Risk Analysis and Management': ['Statistics'],
    'Brand and Advertising': [],
    'Startup Launch and Growth': []
  }
  entrepreneurship_training_program(training_duration, course_details)