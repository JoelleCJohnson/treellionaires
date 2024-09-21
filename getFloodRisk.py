import pandas as pd
import requests

zips = pd.read_csv('tri_county_zips.csv', header=None, names=['zipcode'])
zipcodes = zips.to_dict(orient='records')

headers = {
    'Content-Type': 'application/json',
    'Cookie' : '__Host-next-auth.csrf-token=a99da54a76c06a4c4ead846d2c3992a6db4a655b15c4e86197c566f5c7c769e2%7C7d08e1e6e0183a01dfbf66ac0ea5baa7618ede4ae59ee64c10a9eb3f4f653aad; __Secure-next-auth.callback-url=https%3A%2F%2Ffirststreet.org; __stripe_mid=e79c1159-b261-4f56-b689-13d533f26095a5bed6; AWSALB=TWLhMQyVnMevgtF1JvCmbxjAv5uRthRYnCGgZCrFcx/+3cy5ktOWKReUIsJE8EUOxlrvuJerAI/vqghRgA18EJyqY7NgTuB3kGccDoQrrDgUKvtVFNP7QHPkp9np; AWSALBCORS=TWLhMQyVnMevgtF1JvCmbxjAv5uRthRYnCGgZCrFcx/+3cy5ktOWKReUIsJE8EUOxlrvuJerAI/vqghRgA18EJyqY7NgTuB3kGccDoQrrDgUKvtVFNP7QHPkp9np'
}

for index, row in zips.iterrows():
    zipcode = int(row['zipcode'])

    if pd.isna(zipcode):
        print(f"Invalid zipcode: {zipcode}")
        continue

    payload = {"query":"""
                query ZipByFSID($fsid: Int64!) {
                    zcta (fsid: $fsid) {
                     __typename
                           city { name }
                           state {
                             name
                             shortName
                             fsid
                             totalProperties: propertyConnection {
                               totalCount
                             }
                             air {
                               stats {
                                 worstCities {
                                   name
                                   fsid
                                   air {
                                     days {
                                       outdoorDays {
                                         relativeYear
                                         totalDays
                                         color {
                                           color
                                         }
                                       }
                                     }
                                   }
                                 }
                                 bestCities {
                                   name
                                   fsid
                                 }
                               }
                             }
                             flood {
                               probability {
                                 countSummary {
                                   low
                                   mid
                                   high
                                   relativeYear
                                   returnPeriod
                                 }
                               }
                               stats {
                                 worstCities {
                                   name
                                   fsid
                                   totalProperties: propertyConnection {
                                     totalCount
                                   }
                                   flood {
                                     probability {
                                       countSummary {
                                         low
                                         mid
                                         high
                                         relativeYear
                                         returnPeriod
                                       }
                                     }
                                   }
                                 }
                                 bestCities {
                                   name
                                   fsid
                                   totalProperties: propertyConnection {
                                     totalCount
                                   }
                                   flood {
                                     probability {
                                       countSummary {
                                         low
                                         mid
                                         high
                                         relativeYear
                                         returnPeriod
                                       }
                                     }
                                   }
                                 }
                               }
                             }
                           }
                           county {
                             name
                             flood {
                               floodAdaptationConnection(first:100, filter:{types: [6, 19, 20, 30, 32]}) {
                                 totalCount
                                 edges {
                                   node {
                                     adaptationId
                                     scenario
                                     name
                                     type
                                     serving {
                                       property
                                     }
                                     geometry {
                                       bbox {
                                         coordinates
                                         type
                                       }
                                     }
                                   }
                                 }
                               }
                               unfilteredFloodAdaptationCount: floodAdaptationConnection {
                                 totalCount
                               }
                             }
                             air {
                               nonAttainments {
                                 classification
                                 part
                                 criteriaPollutant {
                                   criteriaPollutantId
                                   name
                                   description
                                 }
                               }
                               population {
                                 totalPopulation
                                 atRisk {
                                   under18
                                   elderly
                                   asthmaPediatric
                                   asthmaAdult
                                   copd
                                   lungCancer
                                   cvDisease
                                   pregnancy
                                   poverty
                                   poc
                                 }
                               }
                             }
                           }
                           name
                           fsid
                           totalAtRiskFlood: propertyConnection(filter:{ floodRisk:{atRisk: true} }) {
                             totalCount
                           }
                           totalProperties: propertyConnection {
                             totalCount
                           }
                           totalPropertiesWithFloodAdaptation: propertyConnection(filter:{ floodAdaptation:{ hasAdaptation: true}}) {
                             totalCount
                           }
                           majorPropertyCount: propertyConnection(
                             filter: {floodFactor: {floodFactorGE: 5}}
                           ) {
                             totalCount
                           }
                           geometry {
                             center {
                               coordinates
                               type
                             }
                             polygon {
                               coordinates
                               type
                             }
                             bbox {
                               coordinates
                               type
                             }
                           }
                         flood {
                           riskDirection
                            exclusion {
                             description
                           }
                           historic{
                             eventId
                             month
                             year
                             name
                             affectedProperties
                             data {
                               count
                               bin
                             }
                           }
                           communityRisk {
                             riskPercentile
                             score
                             facilitiesCount
                             facilitiesCategory {
                               score
                               facilityCategoryId
                               facilitiesCount
                               risks {
                                 year
                                 relativeYear
                                 facilitiesWaterRisk
                                 facilitiesOperationalRisk
                               }
                             }
                           }
                           adaptationConnection {
                             totalCount
                           }
                           probability {
                             countSummary {
                               year
                               relativeYear
                               mid
                               returnPeriod
                             }
                             count {
                               low
                               mid
                               high
                               year
                               relativeYear
                               returnPeriod
                             }
                           }
                           insurance {
                             propertyInsuranceCount
                           }
                         }
                         fire {
                            exclusion {
                             description
                           }
                           communityRisk {
                             riskPercentile
                             score
                             facilitiesCount
                             facilitiesCategory {
                               score
                               facilityCategoryId
                               facilitiesCount
                               risks {
                                 year
                                 relativeYear
                                 facilitiesFireRisk
                               }
                             }
                           }
                           probability {
                             count {
                               count
                               year
                               relativeYear
                             }
                           }
                           prescribedFires: historicConnection(filter: { type: [PRESCRIBED_FIRE] }) {
                             totalCount
                             edges {
                               node {
                                 ... on LocalityFireHistoric {
                                   eventId
                                   name
                                   month
                                   year
                                   area
                                   affectedProperties
                                   eventNearbyProperties
                                   eventAffectedProperties
                                 }
                               }
                             }
                           }
                           historicConnection {
                             totalCount
                             edges {
                               node {
                                 ... on LocalityFireHistoric {
                                   eventId
                                   name
                                   month
                                   year
                                   area
                                   affectedProperties
                                   eventNearbyProperties
                                   eventAffectedProperties
                                 }
                               }
                             }
                           }
                         }
                         heat {
                           coolingEnergyPercentChange
                           hotTemperature
                           exclusion {
                             description
                           }
                           riskLevel
                           atRisk {
                             propertyCount
                             level
                           }
                         temperatureAverageHigh {
                             relativeYear
                             mmt
                           }
                           heatWaves {
                             hotHeatWave {
                               length
                               relativeYear
                               probability
                             }
                           }
                           days {
                             coolingDays{
                               relativeYear
                               days
                             }
                             distribution {
                               relativeYear
                               binLower
                               days
                             }
                             hotDays {
                               relativeYear
                               days
                             }
                             dangerousDays {
                               relativeYear
                               days
                             }
                             healthCautionDays {
                               relativeYear
                               days
                             }
                           }
                         }
                         wind {
                           riskLevel
                           greatestWindRisk
                           hasTornadoRisk
                           hasCycloneRisk
                           hasThunderstormRisk
                           atRisk {
                             level
                             propertyCount
                           }
                           probability{
                             speed {
                               year
                               relativeYear
                               maxGust
                               maxSpeed
                               returnPeriod
                             }
                           }
                           historicConnection(sort:SPEED_DESC) {
                             totalCount
                             edges {
                               cursor
                               node {
                                 ... on LocalityWindHistoricEventThunderstorm {
                                   eventId
                                   eventType
                                   date
                                   year
                                   damages
                                   injuries
                                   fatalities
                                   maxWind
                                 }
                                 ... on LocalityWindHistoricEventTornado {
                                   eventId
                                   eventType
                                   date
                                   year
                                   damages
                                   category {
                                     tornadoCategoryId
                                     rating
                                     isEnhanced
                                     name
                                     minWindSpeed
                                     maxWindSpeed
                                     description
                                   }
                                 }
                                 ... on LocalityWindHistoricEventCyclone {
                                   localWindSpeed
                                   eventId
                                   eventType
                                   windSpeed
                                   name
                                   year
                                   date
                                   categoryAtLandfall {
                                     windCategoryId
                                     name
                                     minWindSpeed
                                     maxWindSpeed
                                   }
                                   categoryMax {
                                     windCategoryId
                                     name
                                     minWindSpeed
                                     maxWindSpeed
                                   }
                                   categoryLocality {
                                     windCategoryId
                                     name
                                     minWindSpeed
                                     maxWindSpeed
                                   }
                                   affectedProperties
                                   hasDetails
                                 }
                               }
                             }
                           }
                         }
                         air {
                           triFacilityConnection {
                             totalCount
                             edges {
                               node {
                                 name
                               }
                             }
                           }
                           days {
                             outdoorDays {
                               color {
                                 color
                                 colorId
                                 description
                               }
                               relativeYear
                               totalDays
                             }
                           }
                           historic {
                             days(filter: {colorID: 3}) {
                               totalDays
                               year
                             }
                           }
                           riskDirection
                           link
                           communityRisk {
                               score
                               scoreScale
                               riskDirection
                               riskPercentileState
                               riskPercentileNational
                           }
                           exclusion {
                               description
                           }
                           atRisk {
                               level
                               propertyCount
                           }
                        }
                         }
                       }
                     """,
                     "variables":{"fsid": zipcode},
                     "operationName":"ZipByFSID"
        }
    data = requests.post("https://firststreet.org/api/fsfapi?", headers=headers, json=payload)
    if data.json():
        print(data.json()['data'])
        if data.json()['data']['zcta']:
            print(data.json()['data']['zcta']['flood']['communityRisk']['riskPercentile'])
        # print(data.json()['data']['zcta']['flood']['communityRisk']['riskPercentile'])
