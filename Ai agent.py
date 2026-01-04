class LearningAdvisorAgent:
    def __init__(self):
        self.year=None 
        self.gpa=None 
        self.goal=None 
    def ask_information(self):
        print ("Ai agent Tu van hoc tap")
        print ("-"*40)
        self.year=int (input("Ban dang hoc o nam may(1-6)?"))
        self.gpa=float(input("Gpa cua ban hien tai la bao nhieu "))
        self.goal=input("Muc tieu hoc tap cua ban")

    def reasoning(self):
        recommendations=[]
        if self.year==1:
            recommendations.append("Hoc python co ban")
            recommendations.append("Toan roi rac")
        elif self.year==2:
            recommendations.append("Hoc cau truc du lieu")
            recommendations.append("Giai tich 2")
        elif self.year==3:
            recommendations.append("Hoc lap trinh huong doi tuong")
            recommendations.append("Co so du lieu")
        elif self.year==4:
            recommendations.append("Phat trien ung dung web")
            recommendations.append("Mang may tinh")
        if self.gpa<2.0:
            recommendations.append("On lai cac kien thuc co ban")
        elif self.gpa>=3.2:
            recommendations.append("Tham gia nghien cuu hoac project nang cao")

        if self.goal=="ai":
            recommendations.extend([
                "Hoc machine learning",
                "Hoc deep learning",
                "Tham gia cac cuoc thi va nckh  ve AI"
            ])    
        elif self.goal=="Data science":
            recommendations.extend([
                "Hoc cac khoa ve xu ly du lieu",
                "Hoc cac cong cu Data science nhu R, Python",
                "Tham gia cac du an ve Data science"
            ])
        elif self.goal=="Web development":
            recommendations.extend([
                "Hoc cac framework web nhu Django, Flask",
                "Tham gia phat trien cac ung dung web",
                "Hoc ve giao thuc HTTP va RESTful API"
            ])
        else :
            recommendations.append("Xac dinh lai muc tieu hoc tap cua ban")
        return recommendations
    def respond (self,recommendations):
        print ("\nLo trinh de xuat cho ban")
        for i,rec in enumerate(recommendations,1):
            print (f"{i}. {rec}")
            print ("\nAi agent da hoan thanh tu van")
if __name__=="__main__":                   
    agent=LearningAdvisorAgent()
    agent.ask_information()
    recs=agent.reasoning()
    agent.respond(recs)

        