import matplotlib.pyplot as plt
import platform
import numpy as np


# 한국어 패치
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm 
        #fm._rebuild() 
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False
        

# 대기 성분 데이터

atmosphere_compositions = {
        '수성' : {
                'composition' : ['K', 'Na', 'O', 'O2', 'etc'],
                'values' : [31.7, 24.9, 9.5, 5.6, 28.3],
                'colors' : ['maroon', 'gold', 'aqua', 'lightskyblue', 'black']
        },
        '금성' : {
                'composition' : ['CO2', 'N2'],
                'values' : [96.5, 3.5],
                'colors' : ['silver', 'limegreen']
        },
        '지구' : {
                'composition' : ['N2', 'O2', 'Ar', 'CO2', 'etc'],
                'values' : [78, 21, 0.93, 0.04, 0.03],
                'colors' : ['limegreen', 'lightskyblue', 'magenta', 'silver', 'black']
        },
        '화성': {
                'composition' : ['CO2', 'Ar', 'N2', 'etc'],
                'values' : [96, 1.93, 1.89, 0.18],
                'colors' : ['silver', 'magenta', 'limegreen', 'black']
        },
        '목성' : {
                'composition' : ['H2', 'He'],
                'values' : [90, 10],
                'colors' : ['forestgreen', 'pink']
        },
        '토성' : {
                'composition' : ['H2', 'He'],
                'values' : [94, 6],
                'colors' : ['forestgreen', 'pink']
        },
        '천왕성' : {
                'composition' : ['H2', 'He', 'CH4'],
                'values' : [83, 15, 2],
                'colors' : ['forestgreen', 'pink', 'navy']
        },
        '해왕성' : {
                'composition' : ['H2', 'He', 'CH4'],
                'values' : [80, 19, 1],
                'colors' : ['forestgreen', 'pink', 'navy']      
        }
}


# 그래프로 보여주기

type = int(input('형식을 입력하세요. [0 : 막대그래프, 1 : 원]'))
planet = input('원하는 태양계의 행성을 입력하세요.')

if type == 0:
      
        # 막대그래프
        if planet in atmosphere_compositions:
                planet_data = atmosphere_compositions[planet]
                composition = planet_data['composition']
                values = planet_data['values']
                colors = planet_data['colors']

                plt.bar(composition, values, color=colors)
                plt.xticks(composition, composition)
                plt.title(f'{planet}의 대기 조성')

                plt.show()
        else:
               print(f'없는 행성을 입력하셨습니다. ({planet})')

elif type == 1:
        # 크기 다른 원

        if planet in atmosphere_compositions:
                planet_data = atmosphere_compositions[planet]
                composition = planet_data['composition']
                values = planet_data['values']
                colors = planet_data['colors']

                # 백분율
                total = sum(values)
                percentages = [value / total for value in values]

                # 각 성분의 백분율을 원의 크기로
                plt.figure(figsize=(8, 8))
                plt.title(f'{planet}의 대기 조성')

                x_center, y_center = 0.5, 0.5  # 원 중심의 초기 위치임
                radius = 0.4  # 원의 초기 반지름

                for i, (composition_name, percentage, color) in enumerate(zip(composition, percentages, colors)):
                        x_offset = radius * 0.8 * (i % 3 - 1)  # 원 중심의 x 좌표 위치 조절
                        y_offset = radius * 0.8 * (i // 3 - 1)  # 원 중심의 y 좌표 위치 조절
                        x = x_center + x_offset
                        y = y_center + y_offset

                        plt.gca().add_patch(plt.Circle((x, y), percentage * radius, color=color, label=composition_name))
                        plt.text(x, y, composition_name, ha='center', va='center')

                plt.axis('equal')
                plt.legend(loc='upper left')
                plt.show()
        else:
                print(f'없는 행성을 입력하셨습니다. : ({planet})')
else:
        print('지원되지 않는 형식입니다.')