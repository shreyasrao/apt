__author__ = 'shreyas'

# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  if(len(site_list)!=len(user_list)): raise ValueError("site_list and user_list are different lengths")

  grouping = {}

  #for site in site_list:
  for i in range(len(site_list)):
    site = site_list[i]
    visitors = set()
    visitors.clear()

    if(grouping.has_key(site)):
      visitors.clear()
    else:
      indices_of_this_site = [j for j, x in enumerate(site_list) if x == site]
      for user_index in indices_of_this_site: visitors.add(user_list[user_index])
      grouping[str(site)] = visitors


  uniqueSites = []
  for site in grouping: uniqueSites.append(site)

  pairSites = []
  for site in uniqueSites:
    for anotherSite in uniqueSites:
      if(site != anotherSite): pairSites.append((site,anotherSite))

  for i in range(len(pairSites)):
    a,b = pairSites[i]
    if(str(a).lower() > str(b).lower()): pairSites[i] = (b,a)


  hits = {}

  for pair in pairSites:
    a = grouping.get(pair[0])
    b = grouping.get(pair[1])
    section = a.intersection(b)
    hits[len(section)] = pair

  #print hits

  maxKey = 0
  for item in hits:
     if(item > maxKey): maxKey = item

  sol = hits[maxKey]
  first = sol[0]
  for i in range(1,len(sol)):
    second = sol[i]
    if(first != second): return (first,second)
