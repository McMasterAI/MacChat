from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('Maci')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train([
    'How can I apply as an international student?',
    'To apply as an international student, visit our university website and follow the admissions process.',
    'What are the admission requirements for international students?',
    'International students must provide transcripts, language proficiency scores, and other required documents. Check our website for detailed information.',
    'Is there financial aid available for international students?',
    'Yes, we offer financial aid and scholarships for eligible international students. Please check our financial aid office for more details.',
    'Can I work on campus as an international student?',
    'Yes, international students are generally allowed to work on campus. However, there are regulations you need to follow. Visit the international student office for guidance.',
    'Are there English language support services for international students?',
    'Certainly! We provide English language support services to help international students improve their language skills. You can find more information on our website.',
    'How do I find housing as an international student?',
    'Our university offers on-campus housing, and we can assist you in finding off-campus housing options. Check the housing services office for details.',
    'What cultural activities are available for international students?',
    'We organize various cultural activities and events for international students to engage with the community. Follow our international student affairs office for updates.',
    'What are the tuition fees for international students?',
    'Tuition fees for international students vary by program. Please check our official website or contact the admissions office for the most accurate and up-to-date information.',
    'Is health insurance mandatory for international students?',
    'Yes, health insurance is mandatory for international students. Our university provides information on affordable health insurance plans during the orientation process.',
    'Can international students work off-campus?',
    'International students may be eligible to work off-campus, but there are regulations to follow. Consult with the international student services office for guidance.',
    'Are there clubs or organizations for international students?',
    'Absolutely! We have several clubs and organizations dedicated to international students, fostering a sense of community. Explore our student activities office for more details.',
    'How do I extend my student visa as an international student?',
    'To extend your student visa, contact the international student services office well in advance. They will guide you through the necessary steps and paperwork.',
    'Are there language exchange programs for international students?',
    'Yes, we encourage language exchange programs to help international students improve their language skills. Check with the language department or international student services for opportunities.',
    'What transportation options are available for international students?',
    'International students have access to public transportation and may also consider carpooling. The transportation office can provide information on local options.',
    'How can I connect with other international students before arriving?',
    'Join our social media groups and forums for incoming international students. Its a great way to connect with others, ask questions, and share experiences.',
    'What resources are available for mental health support for international students?',
    'We prioritize the mental health and well-being of our international students. The counseling center offers confidential support services; visit their website for more information.',
    'How can I get involved in community service as an international student?',
    'Our university has various community service programs. Check with the community engagement office for volunteer opportunities.',
    'What career services are available for international students?',
    'Career services offer support to international students, including resume building, job search assistance, and networking events. Visit the career center for personalized guidance.',
    'Are there internship opportunities for international students?',
    'Yes, international students can explore internship opportunities. The career services office can help you find relevant internships based on your field of study.',
    'Can I bring my family with me as an international student?',
    'In some cases, international students can bring their families. Contact the international student services office for information on dependent visas and family support services.',
    'How can I participate in cultural exchange programs?',
    'Cultural exchange programs are a great way to connect with students from different countries. Check the international student affairs office for upcoming exchange opportunities.',
    'What safety measures are in place for international students?',
    'The safety of our international students is a top priority. Campus security and the international student services office work together to ensure a secure environment.',
    'What sports facilities are available for international students?',
    'International students can access our state-of-the-art sports facilities. Joining intramural sports or fitness classes is a great way to stay active and meet new people.',
    'How can I obtain a student ID card as an international student?',
    'Visit the student services center to obtain your student ID card. It grants you access to various campus facilities and services.',
    'Are there language-specific support groups for international students?',
    'Yes, we have language-specific support groups to help international students connect with others who speak the same language. Inquire at the international student affairs office.',
    'What language proficiency tests are accepted for international admissions?',
    'We accept tests such as TOEFL, IELTS, and Duolingo English Test for language proficiency. Check our admissions page for specific requirements.',
    'Are there orientation programs for international students?',
    'Absolutely! We conduct orientation programs to help international students acclimate to campus life. Visit the orientation office for schedule details.',
    'How can I transfer my credits as an international student?',
    'To transfer credits, submit your official transcripts during the admissions process. The registrars office will evaluate and determine the transferable credits.',
    'What health services are available for international students?',
    'International students have access to our health center for medical services. Health insurance is also available; inquire at the health services office for details.',
    'Can international students apply for research assistant positions?',
    'Yes, international students can apply for research assistant positions. The research office can provide information on available opportunities and application procedures.',
    'How can I extend my student visa for a study abroad program?',
    'To extend your visa for a study abroad program, contact the international student services office well in advance. They will guide you through the necessary steps.',
    'What cultural festivals or events are organized for international students?',
    'We organize cultural festivals and events throughout the year. Follow the international student affairs office for updates on upcoming cultural activities.',
    'Is there a mentorship program for international students?',
    'Yes, we have a mentorship program to pair international students with experienced mentors. Connect with the mentorship coordinator for more information.',
    'Can international students apply for on-campus jobs?',
    'Yes, international students can apply for on-campus jobs. The student employment office can assist you with job listings and the application process.'

])

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print("Maci:", response)
