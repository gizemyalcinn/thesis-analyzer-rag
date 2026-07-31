## LONG PAPER

## Disability-inclusive emergency mobile app requirements

<!-- image -->

<!-- image -->

Lourdes Moreno 1,2 · Angela Diaz-Redondo 1 · José Manuel Masiello-Ruiz 2 · Belén Ruiz-Mezcua 1,2 Paloma Martínez 1

Accepted: 28 May 2025 / Published online: 18 June 2025 © The Author(s) 2025

## Abstract

This study addresses the accessibility challenges in emergency systems for individuals with disabilities by identifying key requirements and proposing communication modalities for inclusive mobile applications. The goal is to align these systems with user needs, legislative directives, and technical standards. A mixed-methods approach was employed, combining focus groups and structured questionnaires to gather insights from 65 participants with diverse disabilities. This method facilitated the exploration of user needs, communication preferences, and accessibility challenges, complemented by a review of existing standards and legislative frameworks to ensure a comprehensive analysis. The study presents a detailed framework of accessibility requirements and communication modalities, including tailored features for specific disabilities, universal design elements for broad usability, and advanced functionalities to enhance emergency response. These contributions highlight the importance of flexibility, adaptability, and user-centered innovation in emergency mobile applications. This research offers a foundational contribution to the design of inclusive emergency systems by integrating user feedback, accessibility standards, and technical advancements. The proposed requirements and communication modalities provide a roadmap for developers to create tools that ensure safety and accessibility for all in critical situations.

Keywords Accessibility · Disability · Mobile applications · Inclusive design · Emergency communication · User-centered requirements

## 1  Introduction

Accessibility in emergency systems is a shared responsibility among designers, developers, and policymakers. These systems must ensure that all individuals, regardless of their abilities, can access critical services during emergencies. Recognizing this need, the European Union (EU) has established legislative frameworks and technical standards to address the challenges faced by people with disabilities. However, significant gaps remain, particularly in emergency systems that still rely heavily on voice communication, which excludes many users.

This study specifically focuses on a mobile application designed to enable individuals with disabilities to directly contact emergency services (112) in Spain during any emergency. The application facilitates user communication with emergency operators through app accessible modalities. It does not aim to cover public alerting systems, situational awareness platforms, volunteer coordination apps, crisis mapping, or crowdsourcing of disaster information. Still, it focuses solely on providing a direct and inclusive emergency communication channel for people with disabilities.

* Lourdes Moreno lmoreno@inf.uc3m.es

1 Computer Science and Engineering Department, Universidad Carlos III de Madrid, Madrid, Spain

2 Centro Español del Subtitulado y La Audiodescripción (CESyA), Madrid, Spain

In 1991, the EU introduced 112 as a unified emergency number across member states, providing free access to emergency services via voice calls. While widely adopted, this system does not adequately serve individuals with hearing impairments, speech difficulties, or deafblindness. Approximately 24% of the EU population has some form of disability, equating to 87 million individuals [6]. In Spain alone, 4.38 million people have disabilities, with mobility issues being the most prevalent (55.7%), followed by sensory disabilities (28.5% with hearing problems and 24% with visual impairments) and communication or learning difficulties (21.3 and 15.8%, respectively) (Observatorio Estatal de la Discapacidad, 2022).

<!-- image -->

·

<!-- image -->

Emergency services play a critical role in safeguarding the well-being of citizens. Ensuring their accessibility is not only a legal obligation but also a step toward fostering social inclusion. Addressing these challenges requires adopting user-centered and inclusive design principles, actively involving individuals with disabilities throughout the development process.

This research, supported by the project 'Sensory and Cognitive Accessibility in the Communication and Management of Telematic and Telephone Services of the Spanish Government (Access2Citizen)', focuses on identifying the accessibility requirements necessary for the development of inclusive emergency mobile applications. By adopting a user-centered design approach, the project involves an interdisciplinary team of computer science researchers, telecommunications experts, and designers-both with and without disabilities. While the project encompasses the design and development of emergency communication solutions, this article specifically addresses the investigation and analysis of accessibility requirements, providing a foundation for creating mobile applications that are effective, inclusive, and compliant with accessibility standards.

The article begins with a review of existing work and accessibility barriers in mobile applications (Sect. 2). Section 3 presents a user engagement study to capture diverse needs, while Sect. 4 outlines the accessibility requirements derived from these analyses. Finally, Sect. 5 concludes the article by summarizing the findings and suggesting future directions, including the validation and refinement of prototypes for accessible emergency applications.

## 2    Overview

This section provides a comprehensive overview of the accessibility barriers faced by individuals with disabilities when using mobile applications. It includes a detailed analysis of the policies, standards, and technical solutions shaping accessibility in emergency mobile tools, as well as a review of existing work in this domain.

## 2.1    Policies, standards, and accessibility in emergency services

Since 2009, the European Union has actively worked to ensure that emergency services are accessible to everyone, particularly individuals with disabilities. Directive 2009/136/EC introduced the concept of 'equivalent access' for users with disabilities, but its lack of clarity and absence of practical alternatives to voice communication significantly limited its impact [12]. This gap was addressed in 2018 with the European Electronic Communications Code (EECC), which expanded the definition of 'emergency calls' to 'emergency communications'. This new approach included text messages, video calls, and real-time text, mandating that these methods must be free of charge and ensure precise user location tracking [13].

<!-- image -->

In 2019, the European Accessibility Act (EAA) marked a significant advancement by harmonizing accessibility requirements for products and services across the EU. The EAA requires emergency services to incorporate synchronized communications, including voice, text, and video, ensuring accessibility for people with disabilities. This directive, set to be fully implemented by 2025, underscores the EU's commitment to universal accessibility and promotes a more inclusive approach to emergency systems [14].

In Spain, the transposition of European directives into national law has resulted in measures such as Royal Decree 1112/2018, which mandates accessibility for public sector websites and mobile applications. Royal Decree 193/2023 [1] and Law 11/2023 [2], which transposes the European Accessibility Act (EAA), further reinforce these provisions by introducing specific requirements for emergency communications. However, challenges persist, particularly due to the reliance on voice-based communication methods, which are not accessible to everyone.

In addition to legal frameworks, accessibility in emergency systems is supported by key technical standards. According to the EAA or Directive (EU) 2019/882 on the accessibility requirements for products and services, public products and services, such as an emergency mobile application, must comply with the UNE-EN 301 549 standard, which establishes accessibility requirements for ICT products and services in Europe [33]. Additionally, ISO 9241-210:2019 emphasizes a user-centered design approach [18]. These standards provide critical guidance to ensure that user interfaces are perceivable, operable, understandable, and robust, thereby improving accessibility for individuals with disabilities in critical situations.

To enhance emergency communications, decision-making tools can be utilized to evaluate alternative solutions such as voice calls, SMS, and mobile applications. These tools assess options based on criteria like usability, accuracy of information, user perception, and response time. Among these, mobile applications stand out as a particularly effective solution, offering advantages such as precise user location tracking, real-time event descriptions, and the capacity to overcome language barriers. Their bi-directional communication capabilities make them especially valuable in situations involving communication disabilities emergencies.

The Pan-European Mobile Emergency Apps (PEMEA) initiative, supported by the European Emergency Number Association (EENA), represents a significant effort to standardize mobile emergency applications across the EU. By ensuring interoperability, privacy, and usability, PEMEA seeks to provide European citizens with a seamless and accessible emergency communication experience, regardless of their location [11]. Despite the progress, challenges such as fragmented development and region-specific applications highlight the need for greater collaboration between public authorities and private developers.

Finally, accessibility requirements for emergency communications include real-time text, synchronization between voice, text, and video, and interoperability with assistive technologies. These requirements ensure that Public Safety Answering Points (PSAPs) can respond using the same communication method employed by the user, providing equitable access to emergency services. However, developing accessible solutions requires not only compliance with legal and technical standards but also consideration of user needs through inclusive design principles.

Given the diverse and complex requirements-legal, normative, technical, and user-centered-this article aims to consolidate these elements into a comprehensive framework. By integrating legal and regulatory guidelines, accessibility standards, and the specific needs of people with disabilities, this work seeks to facilitate the development of inclusive and effective emergency mobile applications.

## 2.2    Accessibility barriers and assistive technology in mobile applications

An accessible mobile application must be designed for everyone, including people with visual, auditory, motor, cognitive, language, or learning disabilities, as well as those with temporary or age-related impairments.

Although the application is specifically designed for individuals with recognized disabilities, it is important to highlight that inclusive design principles can also benefit individuals experiencing temporary impairments (e.g., injuries, temporary loss of hearing or vision) and older adults with age-related limitations. In emergency situations, stress, injuries, or situational barriers can temporarily impair an individual's ability to communicate or navigate mobile applications. Therefore, adopting inclusive design not only addresses the primary target group but also enhances resilience and accessibility for a broader range of users in critical contexts [4].

Accessibility barriers can range from blind users unable to perceive buttons not labeled for screen readers to users outdoors struggling with low-contrast screens due to reflections. For instance, small text may be illegible for individuals with low vision, and complex instructions may be difficult for users with limited language proficiency or reading comprehension [35].

Each disability necessitates specific considerations. Blind users rely on screen readers to convert visual information into voice output or Braille, while individuals with low vision may require features like content enlargement and improved contrast. People with hearing impairments benefit from adjustable audio, clear sound, and textual or haptic alternatives to auditory cues. Deaf users require subtitles, high-quality video for lip reading, or Sign Language support.

Users with motor disabilities may face challenges with small buttons or intricate gestures, and those unable to use their arms may depend on voice controls or alternative input devices. People with dyslexia benefit from clear, straightforward designs, simple texts, and text-to-speech functionality, while individuals with speech impairments may avoid voice input altogether. Similarly, users with cognitive and learning disabilities require interfaces with clear labels, simple navigation, and unambiguous instructions.

For individuals with intellectual disabilities, tailored design solutions are equally important. Features such as pictograms, clear visual cues, and easy-to-read formats can help convey complex information in a more accessible manner. For example, instructions supported by pictograms or symbols can facilitate navigation and understanding, while text written in plain language with short sentences and supported by visual aids ensures better comprehension. Providing alternative ways to interact with the content, such as audio guidance or step-by-step instructions, further enhances usability for this group.

Adhering to accessibility standards such as WCAG 2.1 [34] and EN 301 549 is crucial to ensure these needs are met. Moreover, incorporating assistive technologies like screen readers, Braille displays, speech-to-text systems, and haptic feedback enriches usability and inclusivity. These design solutions not only address the needs of people with disabilities but also enhance the overall user experience, making applications more intuitive and accessible for everyone.

Recent developments have also explored the use of voice assistants and smart speakers as emergency support tools, especially for users with motor impairments or temporary limitations that hinder touch interaction. For example, Amazon's Alexa Emergency Assist allows users to request help via voice commands, which can be crucial when physical access to a phone is impaired. While current regulations prevent these devices from directly calling 112 or 911, they can connect to emergency contacts or monitoring services. Research by Pradhan et al. [26] highlights how people with disabilities repurpose intelligent personal assistants like Alexa or Google Assistant for accessibility. For instance, Amazon's Alexa Emergency Assist allows users to request help via voice commands, which can be crucial when physical access to a phone is impaired. While current regulations prevent direct calls to 112/911, the system connects to monitoring services or emergency contacts, as demonstrated in recent consumer evaluations [29]. In parallel, wearable systems like LifeKey [31] have been designed to support emergency communication for Deaf users via structured visual interfaces, offering an alternative to voice-based interaction.

<!-- image -->

## 2.3    Related work

The use of mobile applications in emergency scenarios has significantly evolved, establishing these tools as critical for improving response and management in critical situations. These advances have allowed mobile applications to overcome the limitations of traditional methods, such as voice calls or SMS, by integrating advanced functionalities like precise geolocation, bidirectional communication, and the provision of relevant incident data.

Repanovici and Nedelcu [28] evaluated three main communication methods in emergencies: voice calls, SMS, and mobile applications, concluding that mobile applications represent the ideal solution for accessing emergency services. However, they highlighted significant barriers, such as the lack of standardization and low adoption rates among users. This analysis is complemented by Gómez et al. [16], who reviewed over 250 mobile applications and identified gaps in terms of functional integration and adaptability to different contexts. Both studies emphasize the need for public-private collaboration to develop more accessible and effective applications.

A user interaction-centered approach was explored by Nass et al. [24] through the RESCUER App, which introduces tailored interaction modes, such as one-click, guided, and chat-based interfaces, optimizing citizen participation during emergencies. De Guzman et al. [7] proposed a mobile application based on geolocation for command centers, improving resource allocation during critical situations by providing real-time data.

In addition to general mobile tools, accessibility for users with specific disabilities has been a key focus. Hosono et al. [17] designed an accessible mobile tool for individuals with hearing impairments, language difficulties, and non-native speakers, utilizing pictograms and tactile interactions to facilitate emergency communication. A similar focus on communication support for Deaf users is found in the work of [25], who developed SOSPhone, a mobile application designed to facilitate emergency communication through an icon-based interface. The app allowed users to construct and send messages semi-automatically using pictograms, reducing the need for written text or voice. User testing showed that the solution was not only accessible to Deaf users but also intuitive for a broader audience. This reinforces the importance of multimodal, visual-first designs in emergency scenarios, particularly when immediate communication is required under stress.

A similar focus on direct emergency access for Deaf users is found in the work of Constantinou et al. [5], who developed and tested an accessible mobile app in Cyprus, enabling people with hearing impairments to contact 112 emergency services without intermediaries. Through four design-evaluation  cycles  involving  74  Deaf  users  and emergency operators, the study demonstrated the effectiveness of direct interaction via accessible text-based interfaces. This approach helped reduce response time and eliminated the need for third-party relay services, reinforcing the value of self-managed communication during crises.

<!-- image -->

Research targeting blind users has identified significant challenges, as highlighted by Rodrigues et al. [30], who noted common obstacles such as difficulties in touchscreen navigation and a lack of non-visual interaction modalities. Similarly, Carvalho et al. [3] emphasized the critical usability and accessibility problems faced by blind users when interacting with mobile applications, such as missing descriptive labels and inconsistent navigation.

For individuals with intellectual disabilities, Dekelver et al. [8] proposed specific design principles, including simplified interfaces and clear visual cues, which have proven effective in empowering users to interact with emergency tools. These insights demonstrate the importance of tailoring mobile application designs to meet the diverse needs of users with disabilities.

Research highlights the importance of addressing the specific accessibility needs of older adults when designing mobile interfaces, emphasizing accessibility and usability features such as simplified navigation and adjustable text sizes [10].

Accessibility in mobile tools specifically designed for emergencies is essential to ensure that all  individuals, regardless of their abilities, can access critical services in challenging situations. Recent studies highlight that despite technological and regulatory advancements, many applications still fail to meet standards such as UNE-EN 301 549. In previous work, the authors conducted preliminary studies [22] and thoroughly examined mobile emergency applications designed for individuals with disabilities. These studies revealed that none of the assessed applications fully complied with accessibility standards. Specific accessibility requirements were either unmet or could not be evaluated due to limitations in the existing application designs [21].

Radianti et al. [27] evaluated disaster information-sharing tools from a universal design perspective, identifying barriers such as the lack of descriptive labels, resizing functions, and compatibility with assistive technologies. Díaz et al. [9] explored co-production as a model for integrating citizens into emergency management, emphasizing the role of technology in ensuring inclusive participation. Finally, Toquero [32] analyzed the use of mobile health technologies (mHealth) during the COVID-19 pandemic, underscoring the importance of user-centered designs to address disparities in access to emergency services.

Further work by Mack et al. [20] focused on social app accessibility for deaf signers, identifying specific barriers such as the absence of captioning for video content and limited tools for creating accessible Sign Language videos.

These findings underline the broader challenges in achieving accessibility across emergency applications and emphasize the need for continued innovation in design practices.

In addition to mobile apps and wearables, Internet of Things (IoT) platforms and accessible public alert systems have emerged as critical components in inclusive emergency response. The adoption of the Common Alerting Protocol (CAP) enables simultaneous dissemination of alerts via multiple channels (e.g., SMS, apps, TV, sirens) and supports rich multimedia formats such as spoken messages, icons, or multilingual text. This allows adaptive devices to present the alert in the most suitable way for the user. For example, a device for blind users could play a synthesized voice message, while for Deaf users, large-font text and color-coded displays could be shown. The FEMA IPAWS system in the U.S. actively promotes CAP to reach all citizens, including those with functional needs, and has developed a standardized set of 48 emergency pictograms to support cognitive and language accessibility [15]. Additional solutions include wall-mounted visual beacons flashing color-coded alerts, offering visibility in public spaces for users with hearing impairments.

Compared to previous studies, which often focus on specific disabilities [3, 17], or on technical or interface innovations [20, 24], this study offers a comprehensive, user-informed framework of accessibility requirements grounded in real-world experience across a range of disability profiles. While existing standards such as EN 301 549 provide a robust baseline for accessibility, our findings highlight gaps between technical compliance and actual usability under stress, particularly in emergency contexts. For instance, features like a simulation mode or streamlined workflows were repeatedly mentioned by users but are rarely addressed in regulatory documents. Moreover, unlike prior work that examines applications in isolation, this study draws from collective input through focus groups, offering a participatory perspective that bridges legal, technical, and experiential dimensions. This added value lies in translating lived experiences into actionable design requirements that anticipate real barriers and optimize the interaction beyond minimum standards.

Building upon our previous technical and normative analysis [21], which evaluated the accessibility of existing emergency mobile applications and websites in Spain, and expanding the preliminary conference study focused on requirements [22], this article incorporates the voices of users with disabilities through in-depth focus groups. The comparison with related work confirms that many current solutions still fall short of expectations-not only in terms of technical compliance, but also regarding usability, interaction flow, and contextual adaptability in emergencies. These findings reinforce the need for participatory approaches that integrate user-centered design with accessibility regulations from the earliest stages of emergency app development.

## 3    Understanding user diversity in emergency mobile applications

To design an accessible and inclusive emergency mobile application, it is essential to understand the diverse needs of potential users, particularly individuals with disabilities. This section delves into the User Analysis phase, which focuses on identifying the interaction needs and accessibility challenges these users face in emergency scenarios. By adopting a User-Centered Design (UCD) approach, the study aims to ensure that the proposed mobile application effectively addresses these challenges.

A diverse sample of 65 participants was analyzed to capture a comprehensive range of user requirements. The research gathered demographic data, insights into technological experiences, and specific needs related to emergency situations through a combination of focus groups and structured questionnaires. This rigorous approach ensures that the mobile application is not only compliant with accessibility standards such as UNE-EN 301 549 but also tailored to realworld user scenarios.

## 3.1    Participants

In this study, a total of 65 users were recruited from various distinguished organizations dedicated to supporting the rights and needs of those with disabilities. Fundación AMAS 1  is an organization that supports, promotes, and defends the rights of people with intellectual disabilities. ONCE 2  is known for its work with individuals with visual impairments, and FOAPS, 3 affiliated with ONCE, focuses specifically on supporting people with deafblindness. These organizations, alongside AICE 4 (the Spanish Federation of Associations of Cochlear Implants), FIAPAS, 5 (Spanish Confederation of Families of Deaf People), CNSE 6 (National Confederation of the Deaf), and AMIRES 7 (Association of Myopia Magna with Retinopathy). Each contributes significantly to the representation, advocacy, and assistance of people with disabilities in Spain. The sample was designed to ensure diversity, considering specific inclusion criteria:

[1 https://  www.  funda  cion-  amas.  org/.](https://www.fundacion-amas.org/)

[2 https://  www.  once.  es/.](https://www.once.es/)

[3 https://  www.  foaps.  es/.](https://www.foaps.es/)

[4 http://  impla  nteco  clear.  org/.](http://implantecoclear.org/)

[5 https://  fiapas.  es/.](https://fiapas.es/)

[6 https://  www.  cnse.  es/.](https://www.cnse.es/)

[7 https://  miopi  amagna.  org/.](https://miopiamagna.org/)

<!-- image -->

- Age: Adults of different ages were involved, from young adults to the elderly;
- Gender: Both genders were addressed, ensuring equitable representation;
- Disability: People with sensory, or cognitive disabilities, as well as the elderly, were incorporated.

As shown in Table 1, the study involved 65 participants, distributed  almost  equally  between  men  (47.69%)  and women (52.31%). Regarding age distribution, participants ranged from young adults aged 18 to 25 years (20.00%) to older people aged 66 years or more (23.08%), with intermediate representation from those aged 26 to 35 years (18.46%), 36 to 50 years (24.62%), and 51 to 65 years (13.85%).

In terms of educational level, most participants had completed secondary education (29.23%) or higher education (33.85%). A smaller proportion had only basic literacy skills (9.23%) or primary education (9.23%), while 18.46% held a university degree or doctorate.

The study also included a wide range of disability types. The following groups of people with disabilities have been distinguished:

- Visual disabilities-Low Vision: Individuals with partial vision loss who may require visual adjustments, such as larger text or increased contrast, among others;
- Visual disabilities-Blindness: Individuals with complete vision loss who rely on non-visual methods of com-

Table 1 Demographic and disability distribution of study participants

- munication, such as screen readers and audio description for audiovisual content;
- Hearing disabilities (oral communicators(comm)): Individuals who use spoken language, lip reading, reading, and writing. They can message and use subtitles for the deaf and hard of hearing (SDH) to access audiovisual content;
- Hearing disabilities (cochlear implant (CI) users): Individuals with hearing disabilities who rely on cochlear implants for auditory support, often supplementing with lip reading or subtitles and benefiting from clear, consistent sound quality;
- Hearing disabilities (Sign Language (SL) users): Individuals who primarily use Sign Language for communication;
- Deafblindness: Individuals with combined hearing and vision loss who use specialized communication methods;
- Mild intellectual disabilities: Individuals who use easyto-read for text content and graphical elements supported by tools such as pictograms;
- Mild multiple disabilities (older people): Individuals with mild impairments in multiple areas, such as sensory or cognitive functions.

This study focused on participants with sensory (visual and hearing), cognitive (intellectual), and age-related multiple mild disabilities. Users with motor impairments were not included in the participant sample, as the project requirements prioritized addressing sensory and cognitive accessibility challenges in emergency communication. Nevertheless, the requirements proposed in this study are aligned with the UNE-EN 301 549 standard, ensuring that accessibility needs for individuals with motor disabilities are also covered in the recommendations.

| Variable          | Category                                  |   Frequency (n) | Percentage (%)   |
|-------------------|-------------------------------------------|-----------------|------------------|
| Gender            | Male                                      |              31 | 47.69%           |
|                   | Female                                    |              34 | 52.31%           |
| Age               | 18-25 years                               |              13 | 20.00%           |
|                   | 26-35 years                               |              12 | 18.46%           |
|                   | 36-50 years                               |              16 | 24.62%           |
|                   | 51-65 years                               |               9 | 13.85%           |
|                   | 66 years or older                         |              15 | 23.08%           |
| Educational Level | Only literate                             |               6 | 9.23%            |
|                   | Primary education                         |               6 | 9.23%            |
|                   | Secondary education                       |              19 | 29.23%           |
|                   | Diploma or Advanced Degree                |              22 | 33.85%           |
|                   | Bachelor's or Doctorate Degree            |              12 | 18.46%           |
| Disability Type   | Visual disabilities-Low Vision            |               6 | 9.23%            |
|                   | Visual disabilities-Blindness             |               6 | 9,24%            |
|                   | Hearing disabilities (oral comm.)         |               6 | 9.23%            |
|                   | Hearing disabilities (CI users            |              19 | 29.23%           |
|                   | Hearing disabilities (SL users)           |               6 | 9.23%            |
|                   | Deafblindness                             |               3 | 4.62%            |
|                   | Mild intellectual disabilities            |               8 | 12.31%           |
|                   | Mild multiple disabilities (older people) |              11 | 16.92%           |

Participants with hearing disabilities were the most represented group, with cochlear implant users forming the majority (29.23%). Additionally, participants included those with visual impairments, such as low vision (9.23%) and total blindness (9.24%), users of Spanish Sign Language (LSE) (9.23%), individuals with mild intellectual disabilities (12.31%), and those with multiple mild disabilities, primarily older people (16.92%). The study also included a smaller group of participants with deafblindness (4.62%).

The participant sample reflects a wide diversity in demographics, educational backgrounds, and types of disabilities, ensuring a holistic representation of potential users. This diversity is critical for identifying a wide range of accessibility needs and challenges.

## 3.2    Method

A mixed-methods approach was employed, combining focus groups and structured questionnaires to gather in-depth insights into user needs, communication preferences, and accessibility challenges. This approach was further complemented by a review of existing standards and legislative frameworks to ensure a comprehensive analysis. The focus group technique was utilized to capture requirements from the perspective of people with disabilities [19, 23]. Focus groups facilitate the evaluation of user needs prior to interface design by providing spontaneous reactions and revealing group dynamics. However, as this method assesses what users say they do rather than how they interact with a product, it was complemented with additional observational techniques, which are discussed later in this article.

Together, these methods offered complementary insights. Focus groups provided qualitative and nuanced perspectives on user preferences and challenges, while structured questionnaires enabled the collection of quantitative data, such as demographics, technology usage patterns, and preferred communication methods.

All focus groups adhered to a strict ethical protocol approved by the Universidad Carlos III de Madrid (Ref: UC3M-CEI22\_17\_MORENO). Measures were implemented to safeguard participants' rights and privacy. A total of 11 focus groups were conducted, each comprising 6 to 9 participants, facilitated by two conductors: a principal and a backup. In addition to gathering feedback on the proposed application, participants shared their previous experiences with emergency services. Collaboration with associations was instrumental in recruiting participants and co-organizing the sessions.

The focus groups represented a diverse range of disabilities, as described in the Participants section, and included 65 users across the following groups: one for individuals with mild intellectual disabilities, two for older people, one for individuals with blindness and deafblindness, three for CI users, one for individuals with oral communication hearing disabilities, one for SL users, and one for individuals with low vision. These sessions not only allowed participants to share experiences and expectations but also revealed common challenges and group-specific dynamics essential for inclusive design.

A structured questionnaire was also employed to collect data on participants' demographics, mobile and application usage, and preferred communication methods (verbal, nonverbal, or mixed).

The insights obtained from this process enhance both accessibility and the overall user experience, ensuring that the application is adaptable to diverse needs while maintaining ease of use.

## 3.3    Procedure

The study followed a structured and ethical process to ensure consistency and reliability across sessions. The steps were as follows:

1. Study introduction: Participants received a detailed explanation of the study, including its purpose, scope, and relevance. This step ensured a clear understanding of their role and allowed them to ask questions;
2. Informed consent: Facilitators obtained participants' informed consent, ensuring their voluntary participation and adherence to strict ethical protocols. The Ethics Committee safeguarded participants' privacy, security, and rights;
3. Demographic questionnaire: Participants completed a questionnaire collecting demographic information (e.g., age, gender, education level), which provided an overview of the sample's characteristics;
4. Technology use and communication channels questionnaire: Facilitators collected data on participants' technology usage patterns (e.g., mobile phone and app use) and their preferred communication channels (verbal, non-verbal, or mixed);
5. Focus group discussion: Sessions were guided by a predefined script (see Appendix A) to explore participants' experiences with emergency services and their feedback on the proposed application;
6. Exploration of communication methods: For groups addressing auditory disabilities, a deeper exploration of preferred communication methods was conducted, focusing on the channels most effective in both every

<!-- image -->

day and emergency contexts (e.g., voice, text, sign language).

This systematic approach ensured the collection of rich, diverse data to identify the needs of users with disabilities. The results of steps 4 and 5, presented in subsequent sections, highlight patterns in technology use, preferred communication methods, and user feedback. Together, these insights provide a strong foundation for tailoring the application to specific accessibility requirements.

## 4    Results: technology use and communication channels questionnaire

## 4.1    Technology use questionnaire results

Table 2 illustrates the frequency of web usage categorized by disability type, highlighting significant variations in engagement levels. Categories represent usage patterns, where 'Never' indicates no web use, 'Very Little' reflects rare use, 'Weekly' indicates use several times a week, 'Daily' denotes daily use, and 'Every Day' refers to consistent multiple daily interactions with web pages. Participants with hearing and visual impairments reported higher daily usage, while those with mild intellectual disabilities exhibited a mixed pattern. Older people with mild multiple disabilities demonstrated the lowest engagement, with more than half never using the web.

Table 2 Web usage frequency by disability type

| Disability type                           | Never (1)   | Very little (2)   | Weekly (3)   | Daily (4)   | Every day (5)   |   Total (n) |
|-------------------------------------------|-------------|-------------------|--------------|-------------|-----------------|-------------|
| Visual disabilities-Low Vision            | 0 (0%)      | 2 (33.3%)         | 0 (0%)       | 4 (66.7%)   | 0 (0%)          |           6 |
| Visual disabilities-Blindness             | 0 (0%)      | 0 (0%)            | 1 (16.7%)    | 5 (83.3%)   | 0 (0%)          |           6 |
| Hearing disabilities (oral comm.)         | 0 (0%)      | 0 (0%)            | 1 (16.7%)    | 5 (83.3%)   | 0 (0%)          |           6 |
| Hearing disabilities (CI users            | 0 (0%)      | 0 (0%)            | 3 (15.8%)    | 0 (0%)      | 16 (84.2%)      |          19 |
| Hearing disabilities (SL users)           | 0 (0%)      | 0 (0%)            | 0 (0%)       | 6 (100%)    | 0 (0%)          |           6 |
| Deafblindness                             | 0 (0%)      | 0 (0%)            | 0 (0%)       | 3 (100%)    | 0 (0%)          |           3 |
| Mild intellectual disabilities            | 0 (0%)      | 2 (25.0%)         | 1 (12.5%)    | 0 (0%)      | 5 (62.5%)       |           8 |
| Mild multiple disabilities (older people) | 6 (54.5%)   | 1 (9.1%)          | 1 (9.1%)     | 3 (27.3%)   | 0 (0%)          |          11 |
| Total                                     | 6 (9.2%)    | 5 (7.7%)          | 7 (10.8%)    | 26 (40.0%)  | 21 (32.3%)      |          65 |

<!-- image -->

Table 3 Mobile usage patterns by disability type

| Disability type                           | Only calls   | Calls + apps   |   Total (n) |
|-------------------------------------------|--------------|----------------|-------------|
| Visual disabilities-Low Vision            | 0 (0.0%)     | 6 (100%)       |           6 |
| Visual disabilities-Blindness             | 0 (0.0%)     | 6 (100%)       |           6 |
| Hearing disabilities (oral comm.)         | 1 (16.7%)    | 5 (83.3%)      |           6 |
| Hearing disabilities (CI users)           | 0 (0.0%)     | 19 (100%)      |          19 |
| Hearing disabilities (SL users)           | 0 (0.0%)     | 6 (100%)       |           6 |
| Deafblindness                             | 0 (0.0%)     | 3 (100%)       |           3 |
| Mild intellectual disabilities            | 1 (12.5%)    | 7 (87.5%)      |           8 |
| Mild multiple disabilities (older people) | 7 (63.6%)    | 4 (36.4%)      |          11 |
| Total                                     | 9            | 56             |          65 |

The findings highlight significant differences in web engagement across user groups, underscoring the importance of tailored design solutions. Low web usage among older people suggests the need for alternative communication channels, such as direct phone calls or offline functionality, to ensure accessibility for users who may lack digital proficiency. On the other hand, the high web engagement reported by visually impaired participants emphasizes the importance of integrating robust web accessibility features into the application. This includes ensuring compatibility with screen readers, enabling effective keyboard navigation, and providing clear and descriptive content. By addressing these specific needs, the application can enhance inclusivity and usability for diverse user groups.

Table 3 illustrates the usage of mobile phones across disability types, showing that most participants use their devices for both calls and applications. Categories represent usage patterns, where 'Only calls' indicates exclusive use of the mobile for phone calls, and 'Calls + apps' refers to combined use for both phone calls and mobile applications. Older people with mild multiple disabilities, however, predominantly use their phones exclusively for calls. These patterns highlight the widespread adoption of mobile apps, with notable variations in usage among older people.

The results underscore the centrality of mobile applications as a primary channel for emergency communication, validated by their frequent use across most disability groups. This widespread adoption highlights the importance of focusing on app-based solutions to deliver accessible and effective emergency services. However, the preference for phone calls observed among older people emphasizes the need to incorporate a simplified call feature within the application. This functionality should enable direct access to emergency services, ensuring that users with lower digital literacy or those who prefer traditional communication methods can seamlessly connect in critical situations. Balancing these elements ensures the application meets the needs of all user groups.

Table 4 presents the frequency of mobile application usage by disability type. Categories represent frequency of mobile application usage, where 'No' indicates no apps use, 'Little' reflects occasional apps use, 'Sometimes' denotes moderate apps use, and 'Frequent' refers to regular or frequent apps use. Most participants, especially those with hearing impairments, visual impairments, and deafblindness, reported frequent app use. In contrast, older people with mild multiple disabilities and participants with mild intellectual disabilities exhibited more varied usage patterns, including limited or no app use. These results emphasize the importance of tailored accessibility interventions to support lower-engagement groups.

The high adoption of mobile applications among key groups, such as participants with hearing and visual impairments, reinforces the necessity of incorporating robust features tailored to diverse user needs. These include screen readers, high-contrast modes, and voice-to-text functionality to ensure usability and inclusivity. However, the lower app usage observed among older people and individuals with mild intellectual disabilities highlights the importance of offering alternative communication methods. Features such as visual aids, intuitive interfaces, and voice commands can bridge this gap, ensuring that the application remains accessible and effective for all users, regardless of their technological proficiency or cognitive abilities.

Table 4 Frequency of mobile application use by disability type

The data highlights significant variations in web, mobile, and application usage across disability types, suggesting potential associations between these factors. To confirm these patterns, statistical analyses were conducted, revealing a significant relationship between disability type and mobile app usage ( χ 2 (21, N = 65) = 40.12, p ≈  0.007, V  ≈  0.45). The rejection of the null hypothesis underscores that disability type significantly influences both the frequency and manner of mobile application use. These findings imply that some groups, such as those with low app usage, may require enhanced accessibility features or alternative communication methods to engage effectively. For example, older people or individuals with mild intellectual disabilities might benefit from simplified interfaces and non-digital communication options. This evidence emphasizes the necessity of tailoring emergency app designs to meet the diverse needs of all user groups, ensuring equitable access and usability.

## 4.2    Communication channels questionnaire results

To  capture  requirements  regarding  how  people  communicate-whether  verbally,  non-verbally,  or  through mixed methods-particularly in the case of individuals with disabilities, an analysis was conducted distinguishing between options such as voice, text, lip reading, Sign Language, pictograms, and their combinations. Table 5 presents the results, illustrating the distribution of communication channels. Each cell represents the absolute frequency of participants using a specific communication channel. For Expression or Communicative Emission (E), categories are: 1 = Voice, 2 = Voice + Text, 5 = SL, 6 = SL + Text,  7 = Voice + Text + SL.  For  Comprehension  or  Communicative  Reception  (C),  categories  are: 1 = Voice,  2 = Voice + Text,  3 = Voice + Lip  Reading, 4 = Voice + Text + Lip  Reading,  5 = SL,  6 = SL + Text, 8 = Voice + Text + SL + Lip Reading, 9 = Pictograms.

Table 5 illustrates the communication channels used by participants across different disability types, distinguishing between expression (communicative emission) and comprehension (communicative reception). Participants with visual disabilities and mild multiple disabilities predominantly relied on voice for both expression and comprehension, reflecting a simpler communication strategy. In contrast, participants with hearing impairments, particularly SL users and CI users, demonstrated a broader reliance on combined methods, such as voice with text, SL, or lip reading. Deafblind participants showed limited variability, favoring specific methods tailored to their dual impairments. Notably, individuals with mild intellectual disabilities and multiple disabilities exhibited distinct patterns, with the former group primarily using voice for expression, while the latter relied solely on voice for comprehension. This diversity underscores the necessity of designing accessible systems that accommodate a range of communication preferences and modalities.

| Disability type\use apps                  | No (1)    | Little (2)   | Sometimes (3)   | Frequent (4)   |   Total (n) |
|-------------------------------------------|-----------|--------------|-----------------|----------------|-------------|
| Visual disabilities-Low Vision            | 0 (0%)    | 1 (16.7%)    | 0 (0%)          | 5 (83.3%)      |           6 |
| Visual disabilities-Blindness             | 0 (0%)    | 0 (0%)       | 0 (0%)          | 6 (100%)       |           6 |
| Hearing disabilities (oral comm.)         | 1 (16.7%) | 0 (0%)       | 0 (0%)          | 5 (83.3%)      |           6 |
| Hearing disabilities (CI users)           | 0 (0%)    | 0 (0%)       | 1 (5.3%)        | 18 (94.7%)     |          19 |
| Hearing disabilities (SL users)           | 0 (0%)    | 0 (0%)       | 0 (0%)          | 6 (100%)       |           6 |
| Deafblindness                             | 0 (0%)    | 0 (0%)       | 0 (0%)          | 3 (100%)       |           3 |
| Mild intellectual disabilities            | 0 (0%)    | 3 (37.5%)    | 1 (12.5%)       | 4 (50.0%)      |           8 |
| Mild multiple disabilities (older people) | 3 (27.3%) | 3 (27.3%)    | 3 (27.3%)       | 2 (18.2%)      |          11 |
| Total                                     | 4 (6.2%)  | 7 (10.8%)    | 5 (7.7%)        | 49 (75.4%)     |          65 |

<!-- image -->

Table 5 Communication channels by disability type

| Disability Type                           |   E 1 |   E2 |   E5 |   E6 |   E7 |   C1 |   C2 |   C3 |   C4 |   C5 |   C6 |   C8 |   C9 |   Total |
|-------------------------------------------|-------|------|------|------|------|------|------|------|------|------|------|------|------|---------|
| Visual disabilities-Low Vision            |     5 |    1 |    0 |    0 |    0 |    5 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |       6 |
| Visual disabilities-Blindness             |     6 |    0 |    0 |    0 |    0 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |       6 |
| Hearing disabilities (oral comm.)         |     4 |    1 |    0 |    0 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    1 |    0 |       6 |
| Hearing disabilities (CI users)           |    10 |    9 |    0 |    0 |    0 |    4 |    3 |    8 |    4 |    0 |    0 |    0 |    0 |      19 |
| Hearing disabilities (SL users)           |     1 |    0 |    4 |    1 |    0 |    0 |    1 |    0 |    0 |    3 |    2 |    0 |    0 |       6 |
| Deafblindness                             |     2 |    1 |    0 |    0 |    0 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |       3 |
| Mild intellectual disabilities            |     8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    8 |       8 |
| Mild multiple disabilities (older people) |    11 |    0 |    0 |    0 |    0 |   11 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |      11 |
| Total                                     |    47 |   12 |    4 |    1 |    1 |   29 |    7 |    9 |    5 |    4 |    2 |    1 |    8 |      65 |

To confirm these observed differences in communication methods and their relationship with disability types, statistical analyses were conducted. The aim was to determine whether the variability in expression and comprehension strategies across groups was statistically significant. These analyses provide a deeper understanding of how individuals with different disabilities adopt specific channels to communicate effectively. The results of the analyses revealed a statistically significant relationship for both the 'expression (communicative emission)' variable ( χ 2 (32, N  =  65)  =  100.2, p &lt;  0.001, V  =  0.72) and the 'comprehension (communicative reception)' variable ( χ 2 (56, N = 65) = 150.3, p &lt;  0.001, V = 0.65). These findings indicate that each disability profile is strongly associated with specific communication channels, both for expressing and understanding information. Consequently, the null hypothesis of independence was rejected, confirming the influence of disability type on communication preferences.

The statistical analyses underline the importance of offering multiple interaction modalities to accommodate the diverse needs of users, such as voice, text, Sign SL, and pictograms. For example, deafblind users require tactile inputs or Braille support, while visually impaired users benefit from screen reader compatibility and high-contrast interfaces. These insights emphasize the necessity of designing flexible emergency applications that integrate multimodal features, ensuring inclusive and effective access to emergency services for all user profiles.

<!-- image -->

The findings underscore the critical need for multimodal interaction capabilities within the emergency application to address the diverse communication preferences of users. Integrating options such as voice, text, SL, and pictograms ensures that individuals with varying abilities can effectively engage with the system. For users with dual impairments, such as deafblind participants, the application must incorporate specialized communication modes like Braille or tactile input. These tailored features not only address unique accessibility needs but also enhance the overall inclusivity and usability of the application, ensuring it meets the requirements of all user groups in emergency situations.

## 4.3    Findings from the questionnaires

The data highlights significant variability in web, mobile, and application usage, as well as communication strategies across disability types. Statistical analyses revealed a strong association between disability type and technology use patterns, emphasizing the need for customized design solutions. For example, groups with lower app usage, such as older people and those with intellectual disabilities, require simpler interfaces and alternative channels. Conversely, high app usage among visually and hearing-impaired users underscores the importance of advanced accessibility features like screen readers and subtitles for deaf.

The study findings highlight several key principles to guide the design of an inclusive and accessible emergency mobile application:

Multimodal communication options, such as text, voice, and SL, must be integrated to accommodate the diverse needs of users with various disabilities;

Simplified navigation, clear and concise instructions, and adjustable features-such as customizable contrast levels and text sizes-are essential to improve user engagement and ensure ease of use;

The application should provide both online and offline functionality to maintain accessibility, regardless of the users' technological proficiency or access to the internet.

By incorporating these principles, the design can effectively address the unique challenges faced by users, ensuring an equitable and user-friendly experience for all.

## 4.4    Focus group results

This section presents the qualitative findings derived from focus group discussions, offering an in-depth analysis of user experiences, preferences, and challenges in interacting with emergency mobile applications. Each subgroup is explored to highlight unique needs, emphasizing their interaction with technology, access to emergency services, and feedback on existing tools.

## 4.4.1    Users with low vision

Participants with low vision expressed a reliance on their smartphones for daily activities, particularly leveraging built-in accessibility features like screen readers. However, many participants reported limited direct experience with emergency applications, often favoring voice calls for their simplicity and immediacy. Text-based communication, especially when paired with screen readers, was preferred for its clarity and accessibility.

Discussions around app design underscored the importance of large, clear buttons, which mitigate the challenges associated with navigating drop-down menus. Participants emphasized that high color contrast and the inheritance of device-level accessibility settings, such as larger text or bold fonts, are crucial to ensuring usability. They also noted the value of adjustable pictogram sizes during app setup to better accommodate diverse visual needs. Feedback on existing emergency apps revealed dissatisfaction with tools that fail to automatically adapt to accessibility settings, highlighting the need for applications that integrate seamlessly with system-level adjustments.

## 4.4.2    Blindness and deafblindness users

For users with blindness or deafblindness, reliance on phone calls remains prevalent due to the intuitive and fast nature of voice communication. Nonetheless, participants pointed to significant barriers, such as the lack of visual feedback during calls, which often leaves them uncertain about their interaction with emergency services. Users suggested that integrating geolocation and real-time contextual alerts could enhance situational awareness, especially in dynamic or hazardous environments.

The group highlighted the need for well-labeled app elements compatible with screen readers, ensuring that every feature is accessible. Participants also recommended features like simulated drills to build familiarity with app functions and trust in its reliability during emergencies. Additionally, the inclusion of camera functionalities to transmit real-time visuals was suggested as a potential way to bridge communication gaps with responders, though challenges persist in its practical implementation for deafblind users.

## 4.4.3    User with hearing disabilities (oral comm.)

Participants with hearing disabilities who rely on oral communication described their experiences with technology as largely positive, though significant barriers persist in noisy environments. Voice calls remain a common method of contacting emergency services, but stress during critical situations often makes direct verbal communication challenging. To address this, participants emphasized the need for alternative communication methods, such as text and pictograms, which provide clarity in high-stress scenarios.

Design preferences included simple, direct-action buttons and a combined interface of text and pictograms. Participants also suggested the pre-registration of health data, such as their level of hearing loss, to help emergency operators tailor communication strategies. Feedback on existing apps pointed to the importance of easily accessible call options and the value of video calls in establishing a sense of human connection during emergencies.

## 4.4.4    Cochlear implant users

CI users frequently rely on updated smartphones, yet many participants were unaware of the existence of official emergency apps. Their use of voice calls is often influenced by environmental noise, which can impair the effectiveness of their implants. The absence of feedback mechanisms, such as subtitles or chat options, further complicates communication during emergencies.

Participants favored app designs that combine pictograms with explanatory text, as these provide clarity without overreliance on auditory inputs. Simple icons with distinct colors were highlighted as essential for minimizing confusion during stressful situations. They also proposed including features that allow users to indicate whether an emergency concerns themselves or another individual, such as a family member, aligning with their preference for multi-profile capabilities.

<!-- image -->

## 4.4.5    Sign language users

SL users predominantly communicate through platforms like SVISUAL 8 for three-way interpreted calls, though they frequently encounter delays in interpreter availability. This limitation underscores the need for quick-access features, such as a 'Come Find Me' button, to expedite help without relying solely on interpreters.

In terms of design, participants advocated for clear pictograms with concise text to cater to varying literacy levels. Color-coded emergency categories were suggested as a way to reduce confusion, particularly during high-stress situations. Additionally, the incorporation of in-app drills was seen as a valuable tool to enhance user confidence and familiarity with emergency protocols.

## 4.4.6    Users with mild intellectual disabilities

Participants with mild intellectual disabilities displayed varying levels of technological proficiency, with younger individuals adapting more quickly than older ones. Voice calls to 112 remained the preferred method for emergency communication due to their simplicity, while awareness of emergency apps was limited. However, interest in using these tools increased when the design was intuitive and adapted to their needs.

A critical observation was the necessity of incorporating Easy-to-Read text formats. This approach simplifies communication by using short, straightforward sentences and clear instructions, ensuring accessibility for users with diverse literacy levels. Participants also emphasized the value of combining text with pictograms to enhance understanding, alongside high-contrast interfaces with minimal navigation complexity. Features such as large emergency call buttons and quick-access commands were identified as essential.

These findings underscore the need for flexible accessibility options, such as enabling Easy-to-Read mode during setup or within the app's settings. By integrating simplified text, visual aids, and intuitive navigation, the app can effectively address the needs of this group, promoting inclusivity and confidence in emergency scenarios.

## 4.4.7    Mild multiple disabilities (older people)

Older people with mild multiple disabilities demonstrated limited familiarity with smartphones and modern applications, reflecting a preference for traditional communication methods, such as voice calls. This group often struggles with the complexity of digital tools, underscoring the need for straightforward, intuitive interfaces.

8 SVIsual  plaeform  enables  real-time  communication  through  sign language  interpreters,  facilitating  interactions  for  Sign  Language users in various contexts. https://  www.  svisu  al.  org/.

<!-- image -->

Participants emphasized the importance of large emergency call buttons, preferably color-coded for easy identification. Registration processes should involve minimal steps and provide clear, step-by-step guidance to avoid confusion. Many participants noted that face-to-face assistance during the registration process would further alleviate barriers, enhancing their confidence in using the app during emergencies.

## 5    Discussion

The findings from the focus groups underscore the necessity of a unified yet flexible design approach to accommodate the diverse communication and interaction needs of users with varying disabilities. This discussion synthesizes the key requirements and design recommendations, distinguishing between common guidelines beneficial to all users and specific adaptations tailored to individual user groups.

## 5.1    Common requirements

Across  all  groups,  several  universal  design  principles emerged as critical for ensuring accessibility:

- Multi-modal interaction: participants consistently highlighted the importance of offering diverse communication channels, including voice, text, sign language, lip reading and pictograms. Emergency situations often impose stress that can impair users' ability to rely on a single mode of communication. Therefore, enabling users to toggle between channels in real time ensures adaptability to situational demands;
- Simplified  navigation:  navigating  through  complex menus during an emergency can be overwhelming. A prominent 'Emergency Call' or 'SOS' button on the main screen, accompanied by a streamlined user flow with minimal steps, is indispensable. Reducing nested menus and providing intuitive layouts can alleviate cognitive load and enhance user confidence;
- Pre-registration and personal profiles: allowing users to store personal information, such as health conditions, preferred communication methods, and emergency contacts, can significantly expedite response times. Multiuser profiles within a single account are particularly beneficial for households with diverse accessibility needs;
- Reliability and trust: emergency applications must be robust, with clear feedback mechanisms to inform users about the status of their interactions. Real-time updates, such as call progress, estimated wait times, or location

- sharing, can reduce anxiety and enhance user trust in the system;
- In-app tutorials and Simulated drills: familiarity with an application's features is crucial for effective use during emergencies. Simulated drills, guided walkthroughs, and accessible tutorials (e.g., videos with subtitles, Easy-toRead text, or SL support) can improve user preparedness and confidence.

## 5.2    Specific requirements by user group

While the common requirements address core accessibility needs, the focus groups revealed additional nuances specific to each disability group:

- Visual disabilities-Low Vision: participants emphasized the importance of adjustable text sizes, high-contrast themes, and the automatic inheritance of device-level accessibility settings. These features ensure seamless integration with users' established workflows;
- Visual disabilities-Blindness and Deafblindness: Visual disabilities-Blindness and Deafblindness: screen-reader compatibility and audio cues are vital to ensure full app functionality. Deafblind users, in particular, require tactile inputs, Braille compatibility, and vibration patterns to compensate for dual sensory impairments. Additionally, participants emphasized the potential benefits of integrating camera functionalities to transmit real-time visuals to emergency responders. This feature could help bridge communication gaps by providing situational context that blind users cannot convey verbally;
- Hearing disabilities (oral comm.): noise-level indicators and on-screen instructions for quieter communication environments can address the challenges posed by auditory noise. Text-based alternatives and lip-readingfriendly video call layouts were identified as critical for effective interaction;
- Hearing disabilities (CI Users): the integration of pictograms alongside concise explanatory text caters to this group's reliance on visual aids in noisy environments. Real-time subtitles or chat options during calls could further enhance usability;
- Hearing disabilities (SL Users): real-time interpretation services remain essential for this group. The inclusion of sign-language videos explaining app functions and colorcoded emergency categories provides additional clarity and accessibility;
- Mild intellectual disabilities: simplified authentication processes, intuitive icons, and clear text labels were recommended to accommodate varied literacy levels. An Easy-to-Read mode that uses plain language and combines text with pictograms is particularly important for this group. A large, prominently displayed SOS button
- with a minimal-click workflow ensures usability for all users;
- Mild multiple disabilities (older people): this group's limited familiarity with technology necessitates straightforward interfaces focused on essential emergency functions. Enlarged text and symbols, coupled with step-bystep guidance, were identified as critical to overcoming barriers.

In conclusion, the diversity of user needs highlights the complexity of designing an inclusive emergency application. By integrating multi-modal communication options, simplifying navigation, and incorporating personalized settings, the app can cater to a broad spectrum of users. Specific features emphasize the importance of tailoring solutions to individual accessibility profiles.

While the accessibility standards, such as UNE-EN 301 549, provide a comprehensive baseline covering a wide range of disabilities and assistive technologies, the focus group findings revealed user-driven requirements that go beyond compliance. Standards ensure that access is technically possible, but users emphasized the need for optimized, simplified, and more intuitive interactions adapted to their specific needs. This reflects the heterogeneity within each disability group and the influence of personal, contextual, or disability-related factors on interaction. Moreover, participants identified context-specific requirements linked to emergency scenarios, such as the inclusion of a simulation mode, which are not typically addressed by general accessibility standards. Conversely, some standard-based requirements were perceived as irrelevant by users depending on their disability type (e.g., screen reader compatibility for users with hearing impairments not using assistive technologies). These findings suggest the value of combining standard compliance with participatory approaches to address real usage needs.

This study presents some limitations. First, although the sample included a diverse set of disabilities, it did not cover motor impairments, as the project prioritized sensory and cognitive needs. Second, all participants had basic familiarity with mobile phone use, a logical inclusion criterion given the app's nature, but this may not reflect the needs of users with limited digital skills. Third, as an exploratory study, the findings are based on user feedback from focus groups and questionnaires, rather than testing in real or simulated emergency settings. Future stages will address these aspects through prototype development and user testing.

These findings offer actionable insights for developers, reinforcing the necessity of a user-centered approach that balances common accessibility standards with customized adaptations. Ensuring that the application meets both universal and specific requirements will enhance its utility and equity, making emergency services accessible to all.

<!-- image -->

## 6    Requirements proposal

The findings from the user study, combined with a thorough review of regulatory frameworks and accessibility standards, have informed the development of a comprehensive set of requirements. These requirements aim to enhance the usability, accessibility, and overall user experience (UX) of emergency mobile applications tailored for individuals with disabilities. Table 6 provides an overview of these requirements, incorporating user feedback and transcending conventional guidelines to address the specific needs of diverse user profiles. This includes functionalities ranging from bidirectional voice communication to advanced geolocation services, each forming an integral component of the application's robust design.

## 6.1    Requirements overview

Table 6 categorizes and describes the proposed requirements, highlighting their relevance to accessibility standards and user needs. The categories include Networkdependent communications, Communication channels, Emergency prerequisites and Regulatory requirements. These categories provide a structured framework to guide developers in creating inclusive applications.

## 6.2    Communication modalities

Table 7 provides a detailed mapping of communication resources required for each disability group. It categorizes the modalities into six key areas to ensure alignment with user needs.

It  is  important  to  note  the  following  comments  in Table 7:

- While not universally required, lip reading can benefit CI users and older people, particularly in noisy environments or when audio quality is low. This feature enhances communication during emergencies;
- While sign language interpretation is critical for SL users, supplementary use of text and pictograms is valuable, especially when interpreters are unavailable, or delays occur;
- Multi benefit features such as Easy-to-Read text, pictograms, and large buttons are particularly helpful for multiple groups. These features demonstrate that inclusivity can provide universal benefits, enhancing usability for a wide range of users.

The requirements and communication modalities outlined in Tables 6 and 7 underscore the complexity of designing inclusive emergency mobile applications.

In conclusion, this requirements proposal serves as a roadmap for developers aiming to create universally accessible emergency applications. By balancing regulatory compliance with user-centered innovation, the proposed design elements can set a new standard for inclusivity, addressing the varied needs of users with disabilities while ensuring reliability and ease of use.

## 7    Conclusions

This research underscores the critical importance of designing accessible emergency systems to safeguard individuals with disabilities. By engaging 65 participants through focus groups and analyzing existing standards, the study presents a comprehensive framework of requirements that address diverse communication modalities and accessibility features. These requirements aim to ensure compliance with legislative directives while fostering inclusivity and usability across a wide range of user needs.

The findings highlight the complexity of creating a universally accessible system that balances tailored accessibility with universal functionalities. While some features may cater more effectively to specific user groups, they often provide broader benefits, illustrating the importance of a flexible design approach. The inclusion of advanced functionalities, such as real-time video transmission, addresses specific needs identified by blind users to convey situational context that would otherwise remain inaccessible, further exemplifying the value of integrating innovative solutions to bridge communication gaps.

Ongoing user testing, iterative refinement, and adherence to accessibility standards are vital to maintaining the effectiveness of these systems in real-world conditions. This holistic approach not only addresses critical gaps in existing applications but also enhances the safety and responsiveness of emergency services for users with disabilities. The insights gained provide a robust foundation for designing adaptable prototypes capable of meeting diverse user needs.

While compliance with accessibility standards is essential, this study shows that user-informed design is key to meeting practical needs in emergency scenarios. Some user requirements go beyond the scope of standards, reflecting context-specific challenges and the diversity within disability groups. This highlights the importance of complementing regulatory compliance with participatory approaches.

Future work will focus on validating and refining these designs through extensive testing, including scenarios with limited communication options, bridging the gap between theoretical guidelines and practical application, and setting

Table 6 Emergency application accessibility requirements list

| Cod   | Name                                | Description                                                                                                                        | Category                           | Subcategory                         |
|-------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|-------------------------------------|
| R1    | Voice communication                 | Default communication method with emergency services; must serve as a backup or sole means when necessary                          | Network-dependent communica- tions | Emergency Services                  |
| R2    | Pictogram usage                     | Pictograms are to be simple, intu- itive, and compatible with text chat; standard or user-validated pictograms are preferred       | Communication channel              | Communication channel User Feedback |
| R3    | Text Chat                           | Essential for users who cannot or prefer not to use the voice channel; should support image sending and receiving                  | Communication channel              | Communication channel User Feedback |
| R4    | Lip reading support                 | Incorporate high-quality video calls to facilitate lip-reading for deaf or hard of hearing users                                   | Communication channel              | Communication channel User Feedback |
| R5    | Sign Language integration           | Video functionality with a Sign Language interpreter service or connection to sign language- capable operators                     | Communication channel              | User Feedback                       |
| R6    | Geolocation                         | Automatic sharing of user's loca- tion with emergency services to provide precise location data                                    | Emergency prerequisites            | User Feedback                       |
| R7    | Bidirectional voice communica- tion | Support bidirectional voice communication for users with diverse needs                                                             | Regulatory requirements            | UNE-EN 301 549                      |
| R8    | Video capability                    | Implement video applications for Sign Language and lip-reading accessibility                                                       | Regulatory requirements            | UNE-EN 301 549                      |
| R9    | Accessible Web                      | Ensure web pages are accessible in line with UNE-EN 301 549/ WCAG 2.1                                                              | Regulatory requirements            | UNE-EN 301 549                      |
| R10   | Accessible non-web docs             | Non-web documents must be accessible according to UNE- EN 301 549                                                                  | Regulatory requirements            | UNE-EN 301 549                      |
| R11   | Perceptible software                | Software should be perceivable by all users, including those with sensory disabilities                                             | Regulatory requirements            | UNE-EN 301 549                      |
| R12   | Operable software                   | Ensure software is operable and navigable for users with motor and cognitive disabilities                                          | Regulatory requirements            | UNE-EN 301 549                      |
| R13   | Understandable software             | Software must be understand- able, using clear language and instructions                                                           | Regulatory requirements            | UNE-EN 301 549                      |
| R14   | Robust software                     | Develop robust software that works across a range of user technologies and assistive devices                                       | Regulatory requirements            | UNE-EN 301 549                      |
| R15   | Accessibility services usage        | Software should utilize available accessibility services effectively                                                               | Regulatory requirements            | UNE-EN 301 549                      |
| R16   | Accessibility features              | Software should support acces- sibility features and user prefer- ences, including Easy-to-Read text options                       | Regulatory requirements            | UNE-EN 301 549                      |
| R17   | Content management technology       | Employ content management technology that supports acces- sibility, including adaptability to user preferences and assistive tools | Regulatory requirements            | UNE-EN 301 549                      |

<!-- image -->

Table 6 (continued)

| Cod   | Name                       | Description                                                                                                         | Category                           | Subcategory              |
|-------|----------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------|--------------------------|
| R18   | Supportive documentation   | Provide accessible documentation and support services adhering to accessibility standards                           | Regulatory requirements            | Accessibility Guidelines |
| R19   | Non-Internet alternatives  | Provision of SMS and other communication methods where internet connection is unavail- able; no cost to user        | Network-dependent communica- tions | Emergency Services       |
| R20   | Visual aid compatibility   | Interface optimized for screen readers and compatible with other visual aids                                        | Regulatory requirements            | Accessibility Guidelines |
| R21   | Privacy in personalization | Ensure secure pre-registration processes, balancing data privacy with obtaining essential user information          | Advanced features                  | User Feedback            |
| R22   | Simulation features        | Include drills and in-app tutori- als for users to familiarize themselves with emergency functions before real use  | Advanced features                  | User Feedback            |
| R23   | Visualizing communication  | Provide real-time updates on call progress, waiting times, and next steps through visual indicators                 | Advanced features                  | User Feedback            |
| R24   | Camera use                 | Enable real-time video transmis- sion to provide situational con- text for responders, particularly for blind users | Advanced features                  | User Feedback            |

## Table 7 Communication resources by disability group

| Disability profile                | Voice com- munication   | Pictogram + text (Sim- ple, High Contrast)   | Text (clear language, high contrast)   | Lip reading support   | Sign language support   | Text (easy-to- read)   |
|-----------------------------------|-------------------------|----------------------------------------------|----------------------------------------|-----------------------|-------------------------|------------------------|
| Visual Disabilities-Low Vision    | YES                     | YES                                          | YES                                    | NO                    | NO                      | YES                    |
| Visual Disabilities-Blindness     | YES                     | NO                                           | YES                                    | NO                    | NO                      | NO                     |
| Deafblindness                     | YES                     | YES                                          | YES                                    | NO                    | NO                      | NO                     |
| Hearing Disabilities (Oral Comm.) | YES                     | YES                                          | YES                                    | YES                   | NO                      | YES                    |
| Hearing Disabilities (CI Users)   | YES                     | YES                                          | YES                                    | NO                    | NO                      | YES                    |
| Hearing Disabilities (SL Users)   | NO                      | YES                                          | YES                                    | NO                    | YES                     | NO                     |
| Mild Intellectual Disabilities    | YES                     | YES                                          | YES                                    | NO                    | NO                      | YES                    |
| Mild Multiple Disabilities        | YES                     | YES                                          | YES                                    | NO                    | NO                      | YES                    |

<!-- image -->

a new benchmark for inclusivity in emergency response technology.

## Appendix A. Basic guidance for focus groups

## Common questions for all groups

| Question                                                                                   | Prompts                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Have you ever been in an emer- gency situation and needed assistance from 112?             | If yes: What channel did you use (e.g., telephone, app)? / What was your experience like? Were there any challenges or barriers? / What would you have modified or changed to make the experi- ence better? / If no: How would you prefer to access emergency services if needed (e.g., tel- ephone, app, other methods)? |
| Have you used or tried to use a mobile app to access 112 services?                         | If yes: What apps did you use? / What was your experience? Were there any specific features that stood out as helpful or problematic?                                                                                                                                                                                     |
| Would you prefer an app inter- face tailored to your needs (e.g., pictograms versus text)? | If yes: Would you register before- hand, or would you prefer imme- diate access without registration? / What type of customization (e.g., font size, colors, layout) would be most useful to you?                                                                                                                         |
| Apps review                                                                                | Share your feedback on the follow- ing / Accessibility features (e.g., voice commands, high contrast) / Registration process (e.g., ease of use, clarity) / Navigation and ease of locating services (e.g., clear menus, intuitive design)                                                                                |
| Do you use apps for booking healthcare services?                                           | What has been your experience? What challenges or barriers have you encountered, if any? / Would features from these apps be useful in an emergency services app?                                                                                                                                                         |

## Group-specific questions

For users with deafblindness or blindness.

| Question                                                              | Prompts                                                                |
|-----------------------------------------------------------------------|------------------------------------------------------------------------|
| Should the app offer high- contrast settings for improved visibility? | What specific color combinations or contrast levels work best for you? |
| If the app included videos, did you find them helpful or neces- sary? | Do you rely on audio descriptions in videos? Why or why not?           |

| Question                                                                                                     | Prompts                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| (Screen reader users) How would you prefer to interact with the app (e.g., buttons, drop-down menus)?        | Are there specific types of inter- faces that you find more chal- lenging with a screen reader? (e.g., scrolling lists, interactive maps) |
| (Screen reader users) What barriers do you encounter while using apps with screen readers?                   | Have you faced issues like unlabeled buttons, inaccessible menus, or lack of feedback? Please elaborate                                   |
| (Screen reader users) What voice commands or shortcuts (e.g., double tap) would you prefer for rapid access? | Would you like predefined shortcuts, or would you prefer to customize them based on your preferences?                                     |

For Users with hearing disabilities (Oral Comm. CI).

| Question                                                                                                                                                       | Prompts                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is lip reading necessary for your communication?                                                                                                               | If yes: What apps do you use for communication (e.g., Zoom, WhatsApp)? / Under what cir- cumstances do you use lip read- ing (e.g., indoors, outdoors)? / What environmental factors support or hinder lip reading in apps? (e.g., lighting, video qual- ity, camera angles) |
| What alternative channels would you consider (e.g., text, voice, pictograms)?                                                                                  | What specific features (e.g., live transcription, pre-written messages) would enhance your communication experience?                                                                                                                                                         |
| What alerts in emergencies and types of notifications (e.g., vibrations, lights, text mes- sages) would be most useful to grab your attention in an emergency? | Would you prefer to customize these notifications, or should the app suggest predefined options? / How important is the ability to combine multiple types of alerts (e.g., vibration and light) in one notification?                                                         |

For users with hearing disabilities (SL Users).

| Question                                                                         | Prompts                                                                                                                                                                                 |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sign language your primary communication method?                              | If yes: Do you use sign language on mobile apps (e.g., Zoom, WhatsApp)? / Under what circumstances do you use sign language (e.g., indoors, outdoors, one-on-one, group conversations)? |
| In emergencies, would video features in apps help you com- municate effectively? | If no video is available, what alternative channels would you prefer (e.g., text-based chat, pre- written messages, pictograms)?                                                        |
| What interpreter characteristics would improve your emer- gency call experience? | Consider aspects like the inter- preter's clothing (e.g., solid colors), background (e.g., plain or clutter-free), and lighting (e.g., well-lit settings)                               |

For users with Low Vision.

<!-- image -->

| Question                                                                                                                  | Prompts                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Which specific visual adjust- ments are most important to you? (e.g., text size, high con- trast colors, glare reduction) | Would you prefer accessibility settings to be configured auto- matically based on your needs, or would you like to customize them manually? |
| Would you like pictograms or text for navigating services, or a combination?                                              | Do you find certain pictograms easier to recognize than others? Would additional labels or descriptions for pictograms be helpful?          |
| If voice input is unavailable, what alternative resource would you prefer?                                                | Would you rely on a virtual key- board, pre-written options, or an assistant feature for navigation?                                        |

For users with mild intellectual disabilities.

| Question                                                                                                                                                           | Prompts                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Would you prefer an app inter- face with pictograms or text?                                                                                                       | Do you find it easier to recognize symbols or images than reading text? Would a combination of both work better for you? / Do you find it easier to understand content with simplified text? (Easy to reading) / Would exam- ples, shorter sentences, or bullet points help you understand information more effectively? |
| What format do you prefer for step-by-step guidance in the app? (e.g., short videos, ani- mated pictograms, simple text)                                           | Have you found any of these formats particularly helpful in other apps? Would you prefer an option to repeat the steps as needed?                                                                                                                                                                                        |
| How would you like to receive immediate feedback in the app to confirm you've performed an action correctly? (e.g., pop-up messages, sounds, clear visual changes) | Would you prefer a combination of these feedback types, or is one method (e.g., sounds) more helpful to you?                                                                                                                                                                                                             |

For users with mild multiple disabilities (older people).

| Question                                                                                        | Prompts                                                                                                                      |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Would you consider using a mobile app for emergency services if it were simple and voice-based? | What features would make you feel more comfortable using such an app? (e.g., large buttons, voice navigation, minimal steps) |
| What barriers stop you from using mobile apps?                                                  | Is it related to lack of familiarity, concerns about complexity, or physical challenges like vision or dexterity?            |
| If an app could call emergency services with a single button, would you use it?                 | Would you prefer the button to initiate a voice call directly, or provide a text option with assistance?                     |

<!-- image -->

| Question                                                    | Prompts                                                                                                                                         |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| How can the app support your needs in case of an emergency? | Would you like it to include features like voice instructions, reminders for emergencies, or direct connection to family members or caregivers? |

Author contributions This manuscript was collaboratively developed by all co-authors, each making significant contributions to its conception, writing and review of the article. LM led the research, conceptualizing the study design and overseeing the methodology, including the focus group and questionnaire design. AD and PM conducted the state-of-the-art review (background, overview) and extensive literature review. JM and BR were primarily responsible for fieldwork, including participant recruitment, organizing focus groups, and data collection. LM conducted the data analysis and synthesized the findings. LM, PM and AD defined the requirements proposal based on the study results.

Funding Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature. This research is supported by the project 'Sensory and Cognitive Accessibility in the Communication and Management of Telematic and Telephone Services of the Spanish Government (Access2Citizen).' The project is led by the Royal Board on Disability (Real Patronato sobre Discapacidad) and managed by the Spanish Center for Subtitling and Audio Description (CESyACentro Español del Subtitulado y la Audiodescripción). It is funded through the Spanish Government's Recovery, Transformation, and Resilience Plan (Plan de Recuperación, Transformación y Resiliencia del Gobierno de España), supported by the European Union's Next Generation EU program. Additionally, this work is partially funded by Grant PID2023-148577OB-C21 and Grant CPP2023-010411 by MICIU/AEI /https://doi.org/10.13039/501100011033and by FEDER, UE. Funding for APC: Universidad Carlos III de Madrid (Agreement CRUE-Madroño 2025).

Data availability The data supporting the  findings  of  this  study are  available  in  anonymized  form  in  the  secure  institutional repository  following  approval  Human  Ethics  declarations  with approval granted by the ethics committee at UC3M (Reference: UC3M-CEI22\_17\_MORENO).

## Declarations

Conflict of interest The authors declare no competing interests.

Human or animal rights Human ethics and approval Human Ethics declarations have been fulflled, with approval granted by the ethics committee at UC3M (Reference: UC3M-CEI22\_17\_MORENO).

Consent to participate Consent to participate Informed consent was obtained from all individual participants included in the study.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

## References

1. BOE. Real Decreto 193/2023, de 21 de marzo, por el que se regulan las condiciones básicas de accesibilidad y no discriminación de las personas con discapacidad para el acceso y utilización de los bienes y servicios a disposición del público. Boletín Oficial del Estado, Núm. 70, 22 de marzo de 2023. (2023a). Retrieved from https://  www.  boe.  es/  buscar/  act.  php?  id=  BOE-A-  2023-  7417
2. BOE. Ley 11/2023, de 8 de mayo, de trasposición de Directivas de la Unión Europea en materia de accesibilidad de determinados productos y servicios, migración de personas altamente cualificadas, tributaria y digitalización de actuaciones notariales y registrales; y por la que se modifica la Ley 12/2011, de 27 de mayo, sobre responsabilidad civil por daños nucleares o producidos por materiales radiactivos. Boletín Oficial del Estado, Núm. 110, 9 de mayo de 2023. (2023b). Retrieved from https://  www.  boe.  es/ buscar/  act.  php?  id=  BOE-A-  2023-  11022
3. Carvalho, M.C.N., Dias, F.S., Reis, A.G.S., Freire, A.P.: Accessibility and usability problems encountered on websites and applications in mobile devices by blind and normal-vision users. In Proceedings of the 33rd Annual ACM Symposium on Applied Computing  (SAC  '18).  (2018).  Association  for  Computing Machinery. https://  doi.  org/  10.  1145/  31671  32.  31673  49
4. Clarkson, P.J., Coleman, R., Keates, S., Lebbon, C.: Inclusive design: Design for the whole population. (2013)
5. Constantinou, V., Ioannou, A., Diaz, P.: Inclusive access to emergency services: an action research project focused on hearingimpaired citizens. Univ. Access Inf. Soc. 16 , 929-937 (2017). https://  doi.  org/  10.  1007/  s10209-  016-  0509-5
6. Council of the EU and the European Council. (n.d.). Disability in the EU: Facts and figures. Retrieved from https://  www.  consi  lium. europa.  eu/  es/  infog  raphi  cs/  disab  ility-  eu-  facts  figur  es/
7. De Guzman, J.B., De Guzman, R.C.C., Ado, R.G.: Mobile emergency response application using geolocation for command centers. Int. J. Comput. Commun. Eng. 3 (4), 235-238 (2014). https:// doi.  org/  10.  7763/  IJCCE.  2014.  V3.  327
8. Dekelver, J., Kultsova, M., Shabalina, O., Borblik, J., Pidoprigora, A., Romanenko, R.: Design of mobile applications for people with intellectual disabilities. In Proceedings of the 11th International Conference on e-Learning and e-Teaching (ICeLeT 2018). Thomas More University College. (2018)
9. Díaz, P., Carroll, J.M., Aedo, I.: Coproduction as an approach to technology-mediated citizen participation in emergency management. Future Internet (2016). https://  doi.  org/  10.  3390/  fi803  0041
10. Díaz-Bossini, J.M., Moreno, L.: Accessibility to mobile interfaces for older people. Procedia Comput. Sci. 27 , 57-66 (2014). https:// doi.  org/  10.  1016/j.  procs.  2014.  02.  008
11. EENA. (n.d.). Pan-European Mobile Emergency Apps. Retrieved from https://  eena.  org
12. European Parliament and Council of the European Union. Directive 2009/136/EC of the European Parliament and of the Council of 25 November 2009 on universal service and users' rights relating to electronic communications networks and services. Official Journal of the European Union. (2009).
13. European Parliament and Council of the European Union. European Electronic Communications Code (EECC). Directive (EU) 2018/1972. Official Journal of the European Union. (2018)
14. European Parliament and Council of the European Union. Directive (EU) 2019/882 on the accessibility requirements for products and services. Official Journal of the European Union. (2019)
15. Federal Emergency Management Agency (FEMA). Alerting people with disabilities and access and functional needs. Integrated Public Alert and Warning System (IPAWS). (2023). https://  www. fema.  gov/  emerg  ency-  manag  ers/  pract  ition  ers/  integ  rated-  publicalert-  warni  ng-  system/  public/  alert  ing-  people-  disab  iliti  es
16. Gómez, D., Bernardos, A.M., Portillo, J.I., Tarrío, P., Casar, J.R.: A review on mobile applications for citizen emergency management. In: Corchado, J.M., et al. (eds.) Highlights on Practical Applications of Agents and Multi-Agent Systems (PAAMS 2013). Springer (2013)
17. Hosono, N., Inoue, H., Nakanishi, M., Tomita, Y.: Urgent mobile tool for hearing impaired, language dysfunction, and foreigners at emergency situation. In: Proceedings of MobileHCI '14: 16th International Conference on Human-Computer Interaction with Mobile Devices and Services Adjunct. ACM. (2014). https://  doi. org/  10.  1145/  26283  63.  26335  68
18.  ISO. ISO 9241-210:2019 Ergonomics of human-system interaction-Part 210: Human-centred design for interactive systems. (2019). Retrieved from https://  www.  iso.  org/  stand  ard/  77520. html
19. Lazar, J., Feng, J. H., Hochheiser, H.: Research Methods in Human-Computer Interaction (2nd ed.). Morgan Kaufmann. (2017)
20. Mack, K., Bragg, D., Morris, M.R., Bos, M.W., Albi, I., MonroyHernández, A.: Social app accessibility for deaf signers. Proc. ACM Human-Comput. Interac. 4 , 1-31 (2020). https://  doi.  org/ 10.  1145/  34151  96
21. Moreno López, L., Díaz Redondo, A.: Panorámica de la accesibilidad de páginas web y aplicaciones móviles de los servicios de emergencia 112. Real Patronato sobre Discapacidad. (2023). Retrieved from https://  www.  siis.  net/  docum  entos/  ficha/  586763.  pdf
22. Moreno, L.,  Díaz-Redondo,  A.,  Masiello  Ruiz,  J.M.,  RuizMezcua, B., Martínez Fernández, P.: Emergency systems democratization:  Disability-inclusive  mobile  app  requirements.  In Proceedings of the XXIV International Conference on Human Computer Interaction (Interacción '24). Association for Computing Machinery. (2024). https://  doi.  org/  10.  1145/  36572  42.  36585  94
23. Morgan, D.L.: Focus Groups as Qualitative Research, 2nd edn. Sage Publications (1996)
24. Nass, C., Jung, J., Groen, E.C., Villela, K., Holl, K.: Interaction modes for emergency mobile apps. Mobile Inf. Syst. (2018). https://  doi.  org/  10.  1155/  2018/  34379  57
25. Paredes, H., Fonseca, B., Cabo, M., Pereira, T., Fernandes, F.: SOSPhone: a mobile application for emergency calls. Univ. Access Inf. Soc. 13 (3), 277-290 (2014). https://  doi.  org/  10.  1007/ s10209-  013-  0318-z
26. Pradhan, A., Mehta, K., Findlater, L.: Accessibility came by accident: Use of voice-controlled intelligent personal assistants by people with disabilities. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI '18). (2018). Association for Computing Machinery. https://  doi.  org/  10.  1145/ 31735  74.  31740  33
27. Radianti, J., Gjøsæter, T., Chen, W.: Universal design of information sharing tools for disaster risk reduction. In: Murayama, Y., Velev, D., Zlateva, P. (eds.) Information Technology in Disaster Risk Reduction (ITDRR 2017), IFIP Advances in Information and Communication Technology. Springer (2019)
28. Repanovici, R., Nedelcu, A.: Mobile emergency notification apps: Current state, barriers, and future potential. IOP Conf. Series Mater. Sci. Eng. 1009 , 012049 (2021). https://  doi.  org/  10.  1088/ 1757-  899X/  1009/1/  012049
29. Reviewed. (2024). Alexa Emergency Assist review: Your voice can be a lifeline. Reviewed. https://  www.  revie  wed.  com/  acces  sibil ity/  conte  nt/  alexa-  emerg  ency-  assist-  review
30. Rodrigues, A., Nicolau, H., Montague, K., Guerreiro, J., Guerreiro, T.: Open challenges of blind people using smartphones. Int.

<!-- image -->

- J. Human-Comput. Interac. 36 (16), 1605-1622 (2020). https://  doi. org/  10.  1080/  10447  318.  2020.  17686  72
31. Slyper, L., Kim, M. K., Ko, Y., Sobek, I. LifeKey: Emergency communication tool for the Deaf. In Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems (CHI EA '16). (2016). Association for Computing Machinery. https://  doi.  org/  10.  1145/  28515  81.  28906  29
32. Toquero, C.M.D.: Mobile healthcare technology for people with disabilities amid the COVID-19 pandemic. Eur. J. Environ. Public Health (2021). https://  doi.  org/  10.  29333/  ejeph/  8551
33. UNE. (2022). UNE-EN 301 549:2022 Accessibility requirements for ICT products and services. Retrieved from https://  www.  une. org/  encue  ntra-  tu-  norma/  busca-  tu-  norma/  norma?c=  N0068  037
34.  World Wide Web Consortium (W3C). (2018). Web Content Accessibility Guidelines (WCAG) 2.1. Retrieved from https:// www.  w3.  org/  TR/  WCAG21/
35. World Wide Web Consortium (W3C)-Web Accessibility Initiative (WAI). (n.d.). Web Accessibility Initiative (WAI). Retrieved from https://  www.  w3.  org/  WAI/

<!-- image -->

Publisher's  Note Springer  Nature  remains  neutral  with  regard  to jurisdictional claims in published maps and institutional affiliations.