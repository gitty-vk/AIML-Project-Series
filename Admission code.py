from transformers import pipeline

class AdmissionChatbot:
    def __init__(self):
        self.user_data = {}
        self.college_info = {
            "fees": "The tuition fees for VIT-AP University is INR 1,95,000 per annum.",
            "hostels": "VIT-AP has 5 boys hostels and 2 girls hostels. They offer dedicated security, advanced facilities, healthy mess, and a clean environment.",
            "faculty": "Many faculty members at VIT-AP are highly qualified with PhDs from top universities in India and abroad. They are known for their commitment to teaching and student learning.",
            "admission_procedures": "Admission to VIT-AP is conducted on a merit basis through the VITEEE (Vellore Institute of Technology Engineering Entrance Examination) and through management quota. The last date to apply is 28th February 2024. Applicants need to submit scanned images of their photograph and signature in the specified format.",
            "programs_offered": "VIT-AP offers a variety of programs including B.E., M.E./M.Tech, M.Sc., BBA, B.Sc., Ph.D., B.A., M.A., B.Com.",
            "required_documents": "For admission, applicants need to submit documents such as Aadhar card/Age proof certificate, X & XII mark sheets, Transfer Certificate/School Leaving Certificate, Migration Certificate, and mark statements of all attempts of the qualifying examination (for 12th marks verification).",
            "contact_information": "For more queries, you can contact VIT-AP University at admission@vitap.com or call 08863 444444. You can also visit their website: vitap.ac.in.",
            "about_university": "VIT-AP University, located near Vijayawada in Andhra Pradesh, is a prestigious institution known for its commitment to academic excellence and holistic student development. Established to provide quality education, VIT-AP offers a wide range of undergraduate, postgraduate, and doctoral programs across various disciplines.",
            "campus_facilities": "The campus boasts state-of-the-art facilities, including modern classrooms, well-equipped laboratories, a central library, and sports facilities. The university is committed to creating a conducive learning environment that fosters innovation, research, and holistic growth.",
            "vision_mission": "VIT-AP's vision is to be a globally recognized institute of academic excellence, producing leaders and entrepreneurs for a sustainable future. The mission is to impart futuristic technical education and instill high patterns of discipline through dedicated faculty, nurturing students with a world-class infrastructure and stimulating environment."
           
        }
        self.context = ""
        self.question_answering_model = pipeline("question-answering")

    def answer_question(self, user_input):
        context = f"{self.context} VIT-AP University offers various programs. If you have specific questions about admission procedures, requirements, or deadlines, feel free to ask."
        response = self.question_answering_model(question=user_input, context=context)
        return response['answer']

    def respond_to_query(self, user_input):
        if 'name' in user_input.lower():
            self.user_data['name'] = user_input
            self.context = f"Hello {self.user_data['name']}! How can I assist you with your VIT-AP admission queries?"
            return self.context

        elif 'contextual understanding' in user_input.lower():
            if 'name' in self.user_data:
                self.context = f"How can I assist you further, {self.user_data['name']}?"
            else:
                self.context = "What is your name?"
            return self.context

        elif '?' in user_input:
            response = self.answer_question(user_input)
            return response

        elif 'admission' in user_input.lower():
            self.context = self.college_info['admission_procedures']
            return self.context

        elif any(keyword in user_input.lower() for keyword in self.college_info.keys()):
            for keyword, response in self.college_info.items():
                if keyword in user_input.lower():
                    return response

        elif 'location' in user_input.lower() or 'area' in user_input.lower():
            return "VIT-AP University is located near Vijayawada, Andhra Pradesh."

        elif 'amount' in user_input.lower() or 'fees' in user_input.lower():
            return self.college_info['fees']

        elif 'documents' in user_input.lower():
            return self.college_info['required_documents']

        elif 'campus' in user_input.lower() or 'facilities' in user_input.lower():
            return self.college_info['campus_facilities']

        else:
            return f"I'm sorry, I couldn't understand that. For more queries, please visit the main website of VIT-AP University at vitap.ac.in."

def chat():
    chatbot = AdmissionChatbot()

    print("Chatbot: Hello! Welcome to the VIT-AP Admission Chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        bot_response = chatbot.respond_to_query(user_input)
        print(f"Chatbot: {bot_response}")

chat()
