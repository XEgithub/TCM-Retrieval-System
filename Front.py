from configparser import ConfigParser
from Back import Backend
from PyQt5.QtWidgets import QTableWidgetItem


class Frontend:
    def __init__(self, interface):
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
        # 读取配置文件
        self.interface = interface
        self.type = 1  # 模式
        self.location = tuple()  # 当前位置
        self.search_area = [list(), list(), list(), list()]  # 检索区
        self.work_area = dict()  # 药方工作区
        # Global Variable
        self.back = Backend()
        # Import function
        self.init_data()
        # Init data

    def init_data(self):
        data = self.back.init(self.type)
        self.set_all_tables(data)
        return 0

    def get_input(self, box_id, input_box, option_box):
        # 当获取到输入触发此函数，然后在下拉框中显示匹配内容
        text = input_box.text()
        if text:
            data = self.back.query_similar_data(box_id, text)
            if data:
                option_box.show()
                self.set_table(option_box, data)
            else:
                option_box.hide()
        else:
            option_box.hide()
        return 0

    def optioned_data(self, box_id, text):
        # 任意模式下，当option被选中时，显示相关数据
        target_indexs = list()
        if box_id in (0, 3):
            # 选中的是子类（症状 or 药）
            target_indexs.append(box_id / 3 + 1)
        else:
            target_indexs.append(box_id - 1)
            target_indexs.append(box_id + 1)
        data = list(range(4))
        data[box_id] = [text]
        for index in target_indexs:
            sub_data = self.back.union_query(box_id, index, text)
            data[index] = sub_data
        self.set_all_tables(data)
        return 0

    def get_data(self, box_id=1, content=1):
        # 录入模式下，当添加按钮被触发时，将输入的内容添加到数据库
        # 如果当前位置不为空，还要添加关系
        return ['3', '2']

    def save_data(self, box_id):
        # if not self.location:
            # text = self.interface.
        return 0

    @staticmethod
    def set_table(table, data_list):
        if data_list:
            row = len(data_list)
            column = len(data_list[0])
            table.setRowCount(row)
            table.setColumnCount(column)
            for r in range(row):
                for c in range(column):
                    table.setItem(r, c, QTableWidgetItem(data_list[r][c]))

    def set_all_tables(self, data):
        cnt = 0
        widgets = list(range(4))
        widgets[0] = self.interface.tablewidgetSymptom
        widgets[1] = self.interface.tablewidgetDisease
        widgets[2] = self.interface.tablewidgetPrescription
        widgets[3] = self.interface.tablewidgetMedicine
        for item in data:
            if type(item) == list and item:
                self.set_table(widgets[cnt], item)
            cnt += 1
        return 0