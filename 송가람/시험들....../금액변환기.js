function formatDrivDistance(number) {
  const tenThousand = Math.floor(number / 10000);
  const formatTenThousand = tenThousand ? tenThousand.toString() + "만" : "";

  const thousand = Math.floor(number / 1000)
    .toString()
    .slice(-1);
  const formatThousand = Number(thousand) ? thousand + "천" : "";

  const rest = number % 1000;
  const formatRest = rest ? rest.toString() : "";

  const answer = formatTenThousand + formatThousand + formatRest;
  return answer;
}

export default formatDrivDistance;
