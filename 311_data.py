# -*- coding: utf-8 -*-
"""
September 24, 2019
Milo Freese
DAT129 - Python 2
Week 3 - 311 Data: Neighborhood report count

"""
import csv

def main():
    neighborhood()
    
# Receives data from 311 reports
# Determines the number of reports from each neighborhood
# Determines the highest and lowest number of reports for all of neighborhoods
def neighborhood():     
# Declare neighborhood variables
    allegheny_center = 0
    allegheny_west = 0
    allentown = 0
    arlington = 0
    arl_heights = 0
    banksville = 0
    bed_dwells = 0
    beechview = 0
    beltzhoover = 0
    bloomfield = 0
    bluff = 0
    bon_air = 0
    brighton_heights = 0
    brookline = 0
    carrick = 0
    cen_bus_dist = 0
    cen_larry = 0
    cen_north = 0
    cen_oak = 0
    chateau = 0
    chartiers = 0
    crafton_heights = 0
    duq_heights = 0
    e_allegheny = 0
    e_carnegie = 0
    e_hills = 0
    e_lib = 0
    elliot = 0
    esplen = 0
    fairywood = 0
    fineview = 0
    friendship = 0
    garfield = 0
    glen_hazel = 0
    greenfield = 0
    hays = 0
    hazelwood = 0
    highland_park = 0
    homewood_n = 0
    homewood_s = 0
    homewood_w = 0
    knoxville = 0
    larimer = 0
    lincoln_place = 0
    lower_larry = 0
    manchester = 0
    middle_hill = 0
    morningside = 0
    mt_oliver = 0
    mt_wash = 0
    new_homestead = 0
    n_oak = 0
    n_point_breeze = 0
    n_shore = 0
    northview_heights = 0
    oakwood = 0
    perry_north = 0
    perry_south = 0
    point_breeze = 0
    n_point_breeze = 0
    polish_hill = 0
    regent_sq = 0
    ridgemont = 0
    shadyside = 0
    sheraden = 0
    s_oak = 0
    s_shore = 0
    s_side_flats = 0
    s_side_slopes = 0
    spring_garden = 0
    squirrel_hill_north = 0
    squirrel_hill_south = 0
    st_clair = 0
    stanton_heights = 0
    strip_dist = 0
    summer_hill = 0
    swisshelm_park = 0
    terrace_village = 0
    troy_hill = 0
    upper_hill = 0
    upper_larry = 0
    w_end = 0
    w_oak = 0
    westwood = 0
    windgap = 0
    
    # Open csv file 
    with open('311data.csv', newline='') as csvfile:
    
        # establish variable to read file as dictionary
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'Allegheny Center' in row['NEIGHBORHOOD']:
                allegheny_center += 1
            elif 'Allegheny West' == row['NEIGHBORHOOD']:
                allegheny_west += 1
            elif 'Allentown' == row['NEIGHBORHOOD']:
                allentown += 1
            elif 'Arlington' == row['NEIGHBORHOOD']:
                arlington += 1
            elif 'Arlington Heights' == row['NEIGHBORHOOD']:
                arl_heights += 1
            elif 'Banksville' == row['NEIGHBORHOOD']:
                banksville += 1
            elif 'Bedford Dwellings' == row['NEIGHBORHOOD']:
                bed_dwells += 1
            elif 'Beechview' == row['NEIGHBORHOOD']:
                beechview += 1
            elif 'Beltzhoover' == row['NEIGHBORHOOD']:
                beltzhoover += 1
            elif 'Bloomfield' in row['NEIGHBORHOOD']:
                bloomfield += 1
            elif 'Bluff' == row['NEIGHBORHOOD']:
                bluff += 1
            elif 'Bon Air' == row['NEIGHBORHOOD']:
                bon_air += 1
            elif 'Brighton Heights' == row['NEIGHBORHOOD']:
                brighton_heights += 1
            elif 'Brookline' == row['NEIGHBORHOOD']:
                brookline += 1
            elif 'Carrick' == row['NEIGHBORHOOD']:
                carrick += 1
            elif 'Central Business District' == row['NEIGHBORHOOD']:
                cen_bus_dist += 1
            elif 'Central Lawrenceville' == row['NEIGHBORHOOD']:
                cen_larry += 1
            elif 'Central North Side' == row['NEIGHBORHOOD']:
                cen_north += 1
            elif 'Central Oakland' == row['NEIGHBORHOOD']:
                cen_oak += 1
            elif 'Chartiers' == row['NEIGHBORHOOD']:
                chartiers += 1
            elif 'Chateau' == row['NEIGHBORHOOD']: 
                chateau += 1
            elif 'Crafton Heights' == row['NEIGHBORHOOD']:
                crafton_heights += 1
            elif 'Duquesne Heights' == row['NEIGHBORHOOD']:
                duq_heights += 1
            elif 'East Allegheny' == row['NEIGHBORHOOD']:
                e_allegheny += 1
            elif 'East Carnegie' == row['NEIGHBORHOOD']:
                e_carnegie += 1
            elif 'East Hills' == row['NEIGHBORHOOD']:
                e_hills += 1
            elif 'East Liberty' == row['NEIGHBORHOOD']:
                e_lib += 1
            elif 'Elliot' == row['NEIGHBORHOOD']:
                elliot += 1
            elif 'Esplen' == row['NEIGHBORHOOD']:
                esplen += 1
            elif 'Fairywood' == row['NEIGHBORHOOD']:
                fairywood += 1
            elif 'Fineview' == row['NEIGHBORHOOD']:
                fineview += 1
            elif 'Friendship' == row['NEIGHBORHOOD']:
                friendship += 1
            elif 'Garfield' == row['NEIGHBORHOOD']:
                garfield += 1
            elif 'Glen Hazel' == row['NEIGHBORHOOD']:
                glen_hazel += 1
            elif 'Greenfield' == row['NEIGHBORHOOD']:
                greenfield += 1
            elif 'Hays' == row['NEIGHBORHOOD']:
                hays += 1
            elif 'Hazelwood' == row['NEIGHBORHOOD']:
                hazelwood += 1
            elif 'Highland Park' == row['NEIGHBORHOOD']:
                highland_park += 1
            elif 'Homewood North' == row['NEIGHBORHOOD']:
                homewood_n += 1
            elif 'Homewood South' == row['NEIGHBORHOOD']:
                homewood_s += 1
            elif 'Homewood West' == row['NEIGHBORHOOD']:
                homewood_w += 1
            elif 'Knoxville' == row['NEIGHBORHOOD']:
                knoxville += 1
            elif 'Larimer' == row['NEIGHBORHOOD']:
                larimer += 1
            elif 'Lincoln Place' == row['NEIGHBORHOOD']:
                lincoln_place += 1
            elif 'Lower Lawrenceville' == row['NEIGHBORHOOD']:
                lower_larry += 1
            elif 'Manchester' == row['NEIGHBORHOOD']:
                manchester += 1
            elif 'Middle Hill' == row['NEIGHBORHOOD']:
                middle_hill += 1
            elif 'Morningside' == row['NEIGHBORHOOD']:
                morningside += 1
            elif 'Mount Oliver' == row['NEIGHBORHOOD']:
                mt_oliver += 1
            elif 'Mount Washington' == row['NEIGHBORHOOD']:
                mt_wash += 1
            elif 'New Homestead' == row['NEIGHBORHOOD']:
                new_homestead += 1
            elif 'North Oakland' == row['NEIGHBORHOOD']:
                n_oak += 1
            elif 'North Point Breeze' == row['NEIGHBORHOOD']:
                n_point_breeze += 1
            elif 'North Shore' == row['NEIGHBORHOOD']:
                n_shore += 1
            elif 'Northview Heights' == row['NEIGHBORHOOD']:
                northview_heights += 1
            elif 'Oakwood' == row['NEIGHBORHOOD']:
                oakwood += 1
            elif 'Perry North' == row['NEIGHBORHOOD']:
                perry_north += 1
            elif 'Perry South' == row['NEIGHBORHOOD']:
                perry_south += 1
            elif 'Point Breeze' == row['NEIGHBORHOOD']:
                point_breeze += 1
            elif 'Point Breeze North' == row['NEIGHBORHOOD']:
                n_point_breeze += 1
            elif 'Polish Hill' == row['NEIGHBORHOOD']:
                polish_hill += 1
            elif 'Regent Square' == row['NEIGHBORHOOD']:
                regent_sq += 1
            elif 'Ridgemont' == row['NEIGHBORHOOD']:
                ridgemont += 1
            elif 'Shadyside' == row['NEIGHBORHOOD']:
                shadyside += 1
            elif 'Sheraden' == row['NEIGHBORHOOD']:
                sheraden += 1
            elif 'South Oakland' == row['NEIGHBORHOOD']:
                s_oak += 1
            elif 'South Shore' == row['NEIGHBORHOOD']:
                s_shore += 1
            elif 'South Side Flats' == row['NEIGHBORHOOD']:
                s_side_flats += 1
            elif 'South Side Slopes' == row['NEIGHBORHOOD']:
                s_side_slopes += 1
            elif 'Spring Garden' == row['NEIGHBORHOOD']: 
                spring_garden += 1
            elif 'Squirrel Hill North' == row['NEIGHBORHOOD']:
                squirrel_hill_north += 1
            elif 'Squirrel HIll South' == row['NEIGHBORHOOD']:
                squirrel_hill_south += 1
            elif 'St. Clair' == row['NEIGHBORHOOD']:
                st_clair += 1
            elif 'Stanton Heights' == row['NEIGHBORHOOD']:
                stanton_heights += 1
            elif 'Strip District' == row['NEIGHBORHOOD']:
                strip_dist += 1
            elif 'Summer Hill' == row['NEIGHBORHOOD']:
                summer_hill += 1 
            elif 'Swisshelm Park' == row['NEIGHBORHOOD']:
                swisshelm_park += 1
            elif 'Terrace Village' == row['NEIGHBORHOOD']:
                terrace_village += 1
            elif 'Troy Hill' == row['NEIGHBORHOOD']:
                troy_hill += 1
            elif 'Upper Hill' == row['NEIGHBORHOOD']:
                upper_hill += 1
            elif 'Upper Lawrenceville' == row['NEIGHBORHOOD']:
                upper_larry += 1
            elif 'West End' == row['NEIGHBORHOOD']:
                w_end += 1
            elif 'West Oakland' == row['NEIGHBORHOOD']:
                w_oak += 1
            elif 'Westwood' == row['NEIGHBORHOOD']:
                westwood += 1
            elif 'Windgap' == row['NEIGHBORHOOD']:
                windgap += 1

# Establish dictionary and assign keys/values
    neighborhood_count = {'Allegheny Center': allegheny_center,
                          'Allegheny West': allegheny_west,
                          'Allentown': allentown,
                          'Arlington': arlington,
                          'Arlington Heights': arl_heights,
                          'Banksville': banksville,
                          'Bedford Dwellings': bed_dwells,
                          'Beechview': beechview,
                          'Beltzhoover': beltzhoover,
                          'Bloomfield': bloomfield,
                          'Bluff': bluff,
                          'Bon Air': bon_air,
                          'Brighton Heights': brighton_heights,
                          'Brookline': brookline,
                          'Carrick': carrick,
                          'Central Business District': cen_bus_dist,
                          'Central Lawrenceville': cen_larry,
                          'Central Oakland': cen_oak,
                          'Chateau': chateau,
                          'Crafton Heights': crafton_heights,
                          'Duquesne Heights': duq_heights,
                          'East Allegheny': e_allegheny,
                          'East Carnegie': e_carnegie,
                          'East Hills': e_hills,
                          'East Liberty': e_lib, 
                          'Esplen': esplen,
                          'Fairywood': fairywood,
                          'Fineview': fineview,
                          'Friendship': friendship,
                          'Garfield': garfield,
                          'Glen Hazel': glen_hazel,
                          'Greenfield': greenfield,
                          'Hays': hays,
                          'Hazelwood': hazelwood,
                          'Highland Park': highland_park,
                          'Homewood North': homewood_n,
                          'Homewood South': homewood_s,
                          'Homewood West': homewood_w,
                          'Knoxville': knoxville,
                          'Larimer': larimer,
                          'Lincoln Place': lincoln_place,
                          'Lower Lawrenceville': lower_larry,
                          'Manchester': manchester,
                          'Middle Hill': middle_hill,
                          'Morningside': morningside,
                          'Mount Washington': mt_wash,
                          'New Homestead': new_homestead,
                          'North Oakland': n_oak,
                          'North Point Breeze': n_point_breeze,
                          'North Shore': n_shore,
                          'Northview Heights': northview_heights,
                          'Oakwood': oakwood,
                          'Perry North': perry_north,
                          'Perry South': perry_south,
                          'Point Breeze': point_breeze,
                          'Polish Hill': polish_hill,
                          'Regent Square': regent_sq,
                          'Ridgemont': ridgemont,
                          'St. Clair': st_clair,
                          'Shadyside': shadyside,
                          'Sheraden': sheraden,
                          'South Oakland': s_oak,
                          'South Shore': s_shore,
                          'South Side Flats': s_side_flats, 
                          'South Side Slopes': s_side_slopes,
                          'Spring Garden': spring_garden,
                          'Squirrel Hill North': squirrel_hill_north,
                          'Stanton Heights': stanton_heights,
                          'Strip District': strip_dist,
                          'Summer Hill': summer_hill,
                          'Swisshelm Park': swisshelm_park,
                          'Terrace Village': terrace_village,
                          'Troy Hill': troy_hill,
                          'Upper Hill': upper_hill,
                          'Upper Lawrenceville': upper_larry,
                          'West End': w_end,
                          'West Oakland': w_oak,
                          'Westwood': westwood,
                          'Windgap': windgap}
    
    # display dictionary
    print(neighborhood_count)
    print()
    
    # determine neighborhood with the highest call count
    high_report = max(neighborhood_count, key=neighborhood_count.get)

    # determine neighborhood with lowest call count
    low_report = min(neighborhood_count, key=neighborhood_count.get)
    
    # declare report number variables
    high_rep_num = 0
    low_rep_num = 0

    # assign high/low call number to variable
    for report in neighborhood_count:
        if high_report == report:
            high_rep_num = neighborhood_count[report]
        if low_report == report:
            low_rep_num = neighborhood_count[report]
    # display high and low of reports
    print('Highest volume of reports:', high_report, '-', high_rep_num)
    print('Lowest volume of reports:', low_report, '-', low_rep_num)

# Execute the main function
if __name__ == "__main__":
    main()