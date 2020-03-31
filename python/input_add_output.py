import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s] %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
def main(file_config):
    input_file_list = file_config["input"]     #  输入的列表位于file_config[“input”]
	input_training_set = input_file_list[0]    #  对应于输入桩的train_1

	######## 输出路径设置 #######
	result_path = os.path.join(os.path.dirname(input_file_list[0]), 'result.txt')
	############################

	######## 处理过程 #######
	file_object = oepn(input_training_set,"rU")
	rst_val = -1
	try:
		for line in file_object:
			line.rstrip('\n')
			int_val = int(line)
			rst_val = int_val + 1
			logging.info("read {}".format(int_val))
	finally:
		file_object.close()

	with open(result_path, 'w', encoding='UTF-8') as f:
		f.write(rst_val)
	logging.info("write {}".format(rst_val))
	########################

	output_file_list = [result_path]   #  对应于输出桩的result, saved_m
	return output_file_list                        #  必须返回输出路径的list


