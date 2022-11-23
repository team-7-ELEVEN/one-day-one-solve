function getPageData(dayTrade, pageSize, pageNumber) {
  // Your code goes here
  const parseTrade = JSON.parse(dayTrade);

  const newArray = parseTrade.reduce(function (acc, current) {
    const found = acc.find(({ user }) => user === current.user);
    if (found) {
      found.countOfStocks = found.countOfStocks + current.countOfStocks;
      // acc.push(found);
    } else {
      acc.push(current);
    }
    return acc;
  }, []);
  console.log(JSON.stringify(newArray));
}

var dayTrade = `[
  {"user": "Rob", "company": "Google", "countOfStocks": 5},
  {"user": "Bill", "company": "Goldman", "countOfStocks": 18},
  {"user": "Rob", "company": "JPMorgan", "countOfStocks": 10},
  {"user": "Dave", "company": "Boeing", "countOfStocks": 10},
  {"user": "Miley", "company": "Microsoft", "countOfStocks": 12}
]`;

console.log(getPageData(dayTrade, 3, 2)); // page size = 3, page number = 2
