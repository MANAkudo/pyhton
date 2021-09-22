#関数定義
def hello():
    for _ in range(10):
        print("hello")


def schooll(school,name):
    print("学校名:",school)
    print("名前:",name)
    return "完了"

school = "東京情報工学院専門学校"
name = "竹井"

result = schooll(school,name)

print(result)