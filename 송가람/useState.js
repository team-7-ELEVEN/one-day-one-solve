const useState = (x = null) => {
  let state = x;
  const setState = (i) => {
    console.log(state);
  };

  return [state, setState];
};

const [state, setState] = useState("1234");
console.log(state);
setState("asdf");
console.log(state);
