from utils.pptcodegenerator import PptCodeGenerator
from utils.structuregenerator import StructureGenerator


def main(input):
    structure_gen = StructureGenerator()
    ppt_gen = PptCodeGenerator()

    # This is the meeting summary
    #text = "meeting_email"
    text=input
    structure = structure_gen.generate_structure(text)
    code = ppt_gen.generate_code(structure)

test='''
Subject: Summary of Meeting - Financial Results and Strategies

Dear Team,
I hope this email finds you well. I would like to provide a summary of our recent meeting regarding our financial results for the third quarter and our strategies for the upcoming year.
Giacomo opened the meeting by welcoming everyone and introducing the agenda. Andrea then presented the financial results, highlighting a net profit of 10 million euros, a 5% increase compared to the same period last year. He also mentioned improvements in our net interest margin, efficiency ratio, and return on equity.
Paola commended the team on these excellent results and asked about the key factors contributing to them. Andrea explained that our ability to attract new customers, particularly in the small and medium-sized businesses segment, careful cost and risk management, and investment in digital innovation were the main drivers.
After discussing the financial results, Giacomo shifted the focus to our strategies for the next year. Marco outlined our priorities, which include consolidating our market position, increasing profitability, and enhancing our reputation. To achieve these goals, we need to continue focusing on customer needs, developing new products and services, strengthening our online presence, and supporting the ecological and social transition. He also acknowledged the challenges of increasing competition, adapting to new regulations, and managing economic uncertainty related to the pandemic.
Giacomo expressed his satisfaction with the clear and coherent strategies presented. He invited the team to add any additional comments or questions. Director E took the opportunity to ask about the financing of our digital innovation projects – whether we plan to increase our capital or rely on external loans. Andrea responded that, currently, our financial position is strong, and we have good access to capital markets. Therefore, there are no plans to increase capital or seek external loans. However, we will continuously monitor our financial situation and evaluate opportunities as they arise.
Giacomo concluded the meeting by thanking everyone for their participation and wishing them a good day. Andrea echoed his sentiments and extended his thanks as well.
If you have any further questions or need additional information, please don't hesitate to reach out.
Best regards,
'''

if __name__ == "__main__":
    text=test
    main(text)
