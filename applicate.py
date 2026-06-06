class energy_estimater:
    def babies(sleep_time, water_intake, hour):
        #ages 5 and under
        sleep = (sleep_time/12)
        water = (water_intake/1.0)
        circadian = 0
        if 6 <= hour < 10:
            circadian = 0.85
        elif 10 <= hour < 12:
            circadian = 1.00
        elif 12 <= hour < 14:
            circadian = 0.55
        elif 15 <= hour < 17:
            circadian = 0.80
        elif 18 <= hour < 20:
            circadian = 0.40
        elif 21 <= hour or hour < 6:
            circadian = 0.15
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)
        if energy > 100:
            energy = 100
        energy -= 7
        return energy
    def children(sleep_time, water_intake, hour):
        #ages 6-12
        sleep = (sleep_time/10.5)
        water = (water_intake/1.2)
        circadian = 0
        if 6 <= hour < 9:
            circadian = 0.95
        elif 10 <= hour < 12:
            circadian = 1.00
        elif 12 <= hour < 14:
            circadian = 0.60
        elif 15 <= hour < 17:
            circadian = 0.85
        elif 18 <= hour < 20:
            circadian = 0.50
        elif 21 <= hour or hour < 5:
            circadian = 0.20
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)-7
        if energy > 100:
            energy = 100
        return energy
    def teens(sleep_time, water_intake, hour):
        #ages 13-18
        sleep = (sleep_time/9)
        water = (water_intake/1.8)
        circadian = 0
        if 6 <= hour < 9:
            circadian = 0.4
        elif 10 <= hour < 12:
            circadian = 0.7
        elif 12 <= hour < 15:
            circadian = 0.9
        elif 15 <= hour < 18:
            circadian = 1.00
        elif 18 <= hour < 21:
            circadian = 0.80
        elif 21 <= hour or hour < 5:
            circadian = 0.20
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)-7
        if energy > 100:
            energy = 100
        return energy
    def youngadults(sleep_time, water_intake, hour):
        #ages 19-30
        sleep = (sleep_time/8)
        water = (water_intake/2.135)
        circadian = 0
        if 6 <= hour < 9:
            circadian = 0.85
        elif 10 <= hour < 12:
            circadian = 1.00
        elif 12 <= hour < 14:
            circadian = 0.60
        elif 15 <= hour < 17:
            circadian = 0.9
        elif 18 <= hour < 20:
            circadian = 0.60
        elif 21 <= hour or hour < 5:
            circadian = 0.20
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)-7
        if energy > 100:
            energy = 100
        return energy
    def adults(sleep_time, water_intake, hour):
        #ages 31-64
        sleep = (sleep_time/8)
        water = (water_intake/2.025)
        circadian = 0
        if 6 <= hour < 9:
            circadian = 0.8
        elif 10 <= hour < 12:
            circadian = 0.95
        elif 12 <= hour < 14:
            circadian = 0.55
        elif 15 <= hour < 17:
            circadian = 0.85
        elif 18 <= hour < 20:
            circadian = 0.50
        elif 21 <= hour or hour< 5:
            circadian = 0.20
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)-7
        if energy > 100:
            energy = 100
        return energy
    def elders(sleep_time, water_intake, hour):
        #65 and up
        sleep = (sleep_time/7.5)
        water = (water_intake/1.75)
        circadian = 0
        if 6 <= hour < 9:
            circadian = 0.95
        elif 10 <= hour < 12:
            circadian = 1.00
        elif 12 <= hour < 14:
            circadian = 0.65
        elif 15 <= hour < 17:
            circadian = 0.75
        elif 18 <= hour < 20:
            circadian = 0.40
        elif 21 <= hour or hour < 5:
            circadian = 0.20
        energy = round(((sleep*0.6)+(water*0.15)+(circadian*0.25))*100)-7
        if energy > 100:
            energy = 100
        return energy
    def select_difficulty(text):

        text = text.lower()
        if any(x in text for x in ['exam', 'test', 'final']):
            score = 35
        elif any(x in text for x in ['essay', 'project', 'research', 'assignment', 'writing']):
            score = 25
        elif any(x in text for x in ['reading', 'study', 'worksheet']):
            score = 15
        elif any(x in text for x in ['email', 'organize', 'cleanup', 'task', 'chores']):
            score = 8
        else:
            score = 15

        if 'important' in text or 'urgent' in text:
            score += 10
        elif 'review' in text or 'simple' in text:
            score -= 5
        return score