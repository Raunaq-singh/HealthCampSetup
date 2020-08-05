# HealthCampSetup

## **Getting Started**
* In a python script, do the following
``` 
from HealthCampSetupGeneticProblem import HealthCampSetupGeneticProblem
```

* Instantiate the imported class with desired parameters

```
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
```
* The inputs are present in the fixedCost file and costForLocation file. FixedCost file indicates the fixed cost for each facility, and costForLocation represents the facility to location cost
 
* Finally run the instantiated model and get the sites where health camps should be setup

```
ga.run()
bestCampSites = ga.population[0]
```

* Also you can get the site where each patient should be sent to using  ***bestIndividualPlan*** method which returns a list of assigned campsite indices to patients. *(e.g. if the returned plan is [0 1 2 1 2] it means the first patient is connected to campsite 0, second and forth patients are connected to campsite 1 and finally third and fifth patients are connected to campsite with index 2)*

```
bestSiteForEachPatient = ga.bestSiteForEachPatient()
```

* Total execution time is also available (in seconds):
```
totalTime = ga.mainLoopElapsedTime
```