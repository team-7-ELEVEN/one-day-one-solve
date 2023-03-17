// const useState = (x = null) => {
//   let state = x;
//   const setState = (i) => {
//     console.log(state);
//   };

//   return [state, setState];
// };

// const [state, setState] = useState("1234");
// console.log(state);
// setState("asdf");
// console.log(state);

function useState(initialValue) {
  var _val = initialValue; // _val은 useState에 의해 만들어진 지역 변수입니다.
  function state() {
    // state는 내부 함수이자 클로저입니다.
    return _val; // state()는 부모 함수에 정의된 _val을 참조합니다.
  }
  function setState(newVal) {
    // 마찬가지
    _val = newVal; // _val를 노출하지 않고 _val를 변경합니다.
  }
  return [state, setState]; // 외부에서 사용하기 위해 함수들을 노출
}
var [foo, setFoo] = useState(0); // 배열 구조분해 사용
console.log(foo()); // 0 출력 - 위에서 넘긴 initialValue
setFoo(1); // useState의 스코프 내부에 있는 _val를 변경합니다.
console.log(foo());
