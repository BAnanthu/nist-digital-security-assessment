"""
          Finding Assessed-Maturity-Level_value
                                                    """
from django.db.models import Avg

from function.models import IdentifyMaturityRoadMap, Identify
from report.models import IdentifyDataSet
from category.models import Category


def assessedMaturityLevel(process_level, policy_level, documentation_level, automation_level):
    ProcessLevel = process_level
    PolicyLevel = policy_level
    DocumentationLevel = documentation_level
    AutomationLevel = automation_level
    total = ProcessLevel + PolicyLevel + DocumentationLevel + AutomationLevel
    last_color = None
    print("total", total)
    number_of_20 = int(total / 20)
    print('number_of_20', number_of_20)
    remainder = total % 20
    print('remainder', remainder)
    # last_color = 'Orange' if (remainder > 0) and (remainder < 10) else 'Grey'
    last_color = 'O' if (remainder > 0) and (remainder < 10) else 'G'
    if remainder > 0:
        assessed_maturity_level_id = number_of_20 + 2 + 1
    else:
        assessed_maturity_level_id = number_of_20 + 2
    """
     Maturity Roadmap (Read More...)
    (Map of sections 20*5, each section if below 10 then Yellow else Grey)			

    """
    maturity_roadmap = [0, 0, 0, 0, 0]
    colors = [None, None, None, None, None]

    if number_of_20 <= 5:
        for i in range(0, number_of_20):
            maturity_roadmap[i] = 20
            # colors[i] = 'Grey'
            colors[i] = 'G'

        if remainder > 0:
            maturity_roadmap[i + 1] = remainder
            colors[i + 1] = last_color

    print(maturity_roadmap, colors)
    return maturity_roadmap, assessed_maturity_level_id, colors


"""
           Finding ad_maturity_weight and SEVERITY
            SEVERITY = (Threat * Likelihood * Impact) / Adjusted Maturity				
                                                                                """


def calcSeverity(primary_threat_value, likelihood_of_threat_value,
                 impact_of_threat_occurrence_value, assessed_maturity_level_value):
    total = primary_threat_value * likelihood_of_threat_value * impact_of_threat_occurrence_value
    print(f"severity {primary_threat_value} * {likelihood_of_threat_value} * {impact_of_threat_occurrence_value}")
    severity = round((total / assessed_maturity_level_value) + 0.1)
    print(f"severity {total} / {assessed_maturity_level_value} =", severity)
    return severity, assessed_maturity_level_value


"""
               Finding level
               If SEVERITY (<800) level = 1 ;
                if (>=800 &&<2800) level = 2 ;
                if (>=2800 &&<5000) level = 3 ;
                if (>=5000) level = 4 ;							
               1-"Low",2-"Medium",3-"High",4-"Critical				
                                                                                  """


def calcLevel(severity):
    if severity < 800:
        level = 1
        description = "Low"
    elif 800 <= severity < 2800:
        level = 2
        description = "Medium"
    elif 2800 <= severity < 5000:
        level = 3
        description = "High"
    elif severity >= 5000:
        level = 4
        description = "Critical"
    else:
        level = 0
        description = "none"

    return level, description


def calcIdentifyAverageByCategory(identify_id, category_id):
    MATURITYSCOREAVERAGE = IdentifyDataSet.objects.filter(
        identify_id=Identify.objects.get(id=identify_id),
        category_id=Category.objects.get(category_id=category_id)).aggregate(Avg('ad_maturity_weight'))
    print(MATURITYSCOREAVERAGE)

    total = MATURITYSCOREAVERAGE['ad_maturity_weight__avg']
    print("total", total)
    number_of_20 = int(total / 20)
    print('number_of_20', number_of_20)
    remainder = total % 20
    print('remainder', remainder)
    # last_color = 'Orange' if (remainder > 0) and (remainder < 10) else 'Grey'
    last_color = 'O' if (remainder > 0) and (remainder < 10) else 'G'
    assessed_maturity_level_id = number_of_20 + 2

    maturity_roadmap = [0, 0, 0, 0, 0]
    colors = [None, None, None, None, None]

    if number_of_20 <= 5:
        index = 0
        if number_of_20 == 0:
            maturity_roadmap[0] = remainder
            # colors[0] = 'Grey'
            colors[0] = 'G'
            assessed_maturity_level_id = 2

        else:
            for i in range(0, number_of_20):
                maturity_roadmap[i] = 20
                # colors[i] = 'Grey'
                colors[i] = 'G'
                index = i

            if remainder > 0:
                maturity_roadmap[index + 1] = remainder
                colors[index + 1] = last_color

    print(maturity_roadmap, colors)
    MATURITYROADMAPAVG = (maturity_roadmap, colors, assessed_maturity_level_id)
    print(MATURITYROADMAPAVG)

    THREATSEVERITYAVG = IdentifyDataSet.objects.filter(
        identify_id=Identify.objects.get(id=identify_id),
        category_id=Category.objects.get(category_id=category_id)).aggregate(Avg('severity'))
    print(THREATSEVERITYAVG['severity__avg'])
    print(calcLevel(THREATSEVERITYAVG['severity__avg']))
    THREATSEVERITYAVG = calcLevel(THREATSEVERITYAVG['severity__avg'])

    # CALCULATEDPRIORITYAVG =
    return MATURITYSCOREAVERAGE['ad_maturity_weight__avg'], MATURITYROADMAPAVG[2], THREATSEVERITYAVG[0]

# calcIdentifyAverageByCategory(2, 1)
