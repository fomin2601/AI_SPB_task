from pptx import Presentation

info = {
    'project_name': 'Unspot',
    'problem': '',
    'definition': """Система UnSpot – это программное обеспечение для бронирования,
                  позволяющее сотрудникам временно резервировать для себя любое незакрепленное 
                  рабочее место в офисе компании""",
    'solution': 'фывфыв',
    'market': 'фывфы',
    'competitors': 'фвыфв',
    'business_model': 'фвыфы',
    'traction_finance': 'фвфвы',
    'team_and_board': 'фывфыв',
    'investitions': 'фвыв',
    'roadmap': 'фывыфвфы',
    'contacts': '12345',
}

def create_slide(prs, info, content, slide_type=1):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = content
    subtitle.text = info[content]

prs = Presentation()

title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = info['project_name']
subtitle.text = "python-pptx was here!"

for key in info:
    create_slide(prs, info, key, slide_type=1)

prs.save('test.pptx')