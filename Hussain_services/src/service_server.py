#!/usr/bin/env python
import rospy
from Hussain_services.srv import WordCount, WordCountResponse
def count_words(request):
	return len(request.words.split())# num of words
rospy.init_node('service_server')
service = rospy.Service(# register service
	'word_count',# service name
	WordCount,# service type
	count_words# function service provides
)
rospy.spin()