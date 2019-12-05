#encoding=utf8
import os
import sys
import json
import numpy as np
import pandas as pd
import time

sys.path.append('src/')
from tools import get_list


		
class YY(object):

	def __init__(self):

		self.title_list =  ['公开（公告）号', '公开（公告）日', '申请号', '申请日','申请人','标准化申请人',	
		'标准化当前专利权人', '申请人国别代码', '申请人省市代码', 
		'中国申请人地市',	'中国申请人区县','申请人地址', '申请人类型', '当前专利权人', '优先权信息',	
		'当前法律状态','专利有效性',	'首次公开日',	'授权公告日','专利类型', 
		'主分类号','国民经济分类', '转让人', '受让人','转让执行日'] + ['生效日', 'p1', 'p2', 'a1', 'a2', 'code1', 'code2', 'pro1','city1', 'pro2', 'city2']

	def map(self, input):
		"""
		统计专利的合作数据, 作为Y
		year + univ + 和别人合作数
		"""
		college_list = get_list('college_list.txt')

		if not os.path.exists('data.patent_pair'):
			os.system('cat ' + input['patent_dir'] +'/* > data.patent_pair')

		patent_dict = {}
		for line in open('data.patent_pair'):
			items = line.strip().split('\t')
			info = dict(zip(self.title_list, items))
			
			apply_year = info['申请日'][:4]
			apply_person = info['申请人']

			hit_college = []    # 可能多个
			for college in college_list:
				if college in apply_person:
					hit_college.append(college)
			#
			for college in hit_college:
				key = apply_year + '\t' + college
				if key not in patent_dict:
					patent_dict[key] = 0
				patent_dict[key] += 1


		return {'yy_dict': patent_dict}
	