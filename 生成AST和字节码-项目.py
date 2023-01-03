import dis
import os
import ast


# 对所有文件夹打标签并遍历文件夹下所有后缀为.py的文件，对于每一个.py文件生成一个对应的.ast和.dis文件
def processDir(root_1_path, project_path, new_root_1_path, new_project_path):
    error_msg = ""
    for root, dirs, files in os.walk(str(os.path.join(root_1_path, project_path))):
        tempRoot = os.path.join(new_root_1_path, new_project_path) + root.replace(root_1_path, "").replace(project_path,
                                                                                                           "")
        if not os.path.exists(tempRoot):
            os.makedirs(tempRoot)
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                try:
                    s = open(root + "\\" + file, encoding="utf8").read()
                    co = compile(s, file.replace(".py", ".dis"), 'exec')
                    print("正在处理文件：", root + "\\" + file + "")
                    # print(dis.dis(co))
                    dis.dis(co, file=open(
                        os.path.join(tempRoot + "/" + new_project_path + "#" + file.replace(".py", ".dis")), 'w',
                        encoding="utf8"))
                    # print("这是文件：", root + "\\" + file + "的AST：")
                    # print(ast.dump(ast.parse(s), indent=4))
                    with open(os.path.join(tempRoot + "/" + new_project_path + "#" + file.replace(".py", ".ast")), "w",
                              encoding="utf8") as f:
                        f.write(ast.dump(ast.parse(s), indent=4))
                except Exception as e:
                    print("报错啦！", e)
                    error_msg += root + "\\" + file + "：" + str(e) + "\n"
    return error_msg


def main():
    # basePath = "常用库\\Web框架\\bottle"
    root_1_path = "gitdown"
    root_2_path = ""
    # project_path = "Test"
    new_root_1_path = root_1_path + "-ast-dis"
    new_root_2_path = ""
    record_msg = ""
    error_msg = ""
    for i in range(len(os.listdir(root_1_path))):
        error_msg += processDir(root_1_path, os.path.join(os.listdir(root_1_path)[i]), new_root_1_path,
                                str(i))
        record_msg += os.listdir(root_1_path)[i] + "/" + os.path.join(root_1_path,
                                                                      os.listdir(root_1_path)[i]) + "--->" + str(
            i) + "\n"
    # processDir(root_1_path, root_2_path, project_path, new_root_1_path, new_root_2_path)
    with open("record-" + root_1_path + ".txt", "w", encoding="utf8") as f:
        f.write(record_msg)
        f.write("\n--------------------------\n")
        f.write(error_msg)


if __name__ == '__main__':
    main()
    # print(os.listdir("./"))
