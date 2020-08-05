from HealthCampSetupGeneticProblem import HealthCampSetupGeneticProblem
from numpy import genfromtxt

potentialCampsitesFixedCost = genfromtxt("fixedCost.txt")
campsiteToPatientCost = genfromtxt("costForLocations.txt")

ga = HealthCampSetupGeneticProblem(
    potentialCampsitesFixedCost,
    campsiteToPatientCost,
    mutationRate = 0.01,
    crossoverMaskRate = 0.4,
    eliteFraction = 1/3,
    populationSize = 150,
    cacheParam = 50,
    maxRank = 2.5,
    minRank = 0.712,
    maxGenerations = 1000,
    nRepeat = 500,
    printProgress = True
)

ga.run()
bestCampSites = ga.population[0]
print("\nBest Individual is = ", bestCampSites)

bestSiteForEachPatient = ga.bestSiteForEachPatient()
print("\nBest Plan is = ", bestSiteForEachPatient)

totalTime = ga.mainLoopElapsedTime
print("\nTotal time is = ", totalTime)