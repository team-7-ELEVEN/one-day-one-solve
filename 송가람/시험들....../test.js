const orderByLength = (arr) => {
  const orderedArr = [...arr];
  orderedArr.sort((prev, cur) => {
    if (prev.length > cur.length) return 1;
    if (prev.length < cur.length) return -1;
  });

  return orderedArr;
};

const convertStr = (str) => {
  const arr = str.split(" ");
  const ans = [];

  arr.forEach((el) => {
    const convertStr = el.toUpperCase().replace(/.$/, (el) => el.toLowerCase());
    ans.push(convertStr);
  });

  return ans.join(" ");
};

// useEffect를 활용하여

// "LifeCycle" 컴포넌트가 생성되면(componentDidMount) "Hello world!"

// "LifeCycle" 컴포넌트가 사라지기 전에(componentWillUnmount) "Bye world!"

// 를 console.log로 출력하는 코드를 만들어주세요.

// * 컴포넌트 마운트 후 "Hello world!" 출력

// * 컴포넌트 사라지기 전에 "Bye world!" 출력

// [예]

// import { useEffect } from "react";

// const LifeCycle = () => {
//   return <></>
// }

// export default LifeCycle;

// [3-2]

// 아래와 같이 "Listing" 컴포넌트의 인자 props가 주어졌을때, 모든 applicant를 랜더링하는 코드를 완성시켜주세요.

const props = {
  applicant: [
    {
      id: 1,
      name: "김백수",
    },
    {
      id: 2,
      name: "박보검",
    },
    {
      id: 3,
      name: "김밥",
    },
    {
      id: 4,
      name: "유남생",
    },
  ],
};

// 랜더링 결과 예시

<div id="list">
  <div key={1}>김백수</div>
  ...
</div>;

// * 각 applicant를 담는 엘리먼트에 key=id

// * 각 applicant안에는 name이 보여야함

// [예]

export const Listing = ({ applicant }) => {
  return (
    <div id="list">
      {applicant &&
        applicant.map((data) => <div key={data.id}>{data.name}</div>)}
    </div>
  );
};

// [3-3]

// password input에 비밀번호 양식이 맞을때만 확인 버튼이 클릭 가능하게 해주세요.

// 최대 입력 가능한 글자수는 20자입니다.

// 비밀번호 양식은 영문, 숫자, 특수문자 포함 10 - 20자 입니다.

// * input[type="text"] 에 최대 문자열 20까지 입력 가능

// * 이 값에 따라서 input[type="submit"]의 disable 상태가 바뀝니다.

// [예]

import { useState } from "react";

const PwInput = () => {
  const [password, setPassword] = useState("");

  const passwordValidation = (password) => {
    return password
      .toLowerCase()
      .match(
        /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[`~!@#$%^&*()\-_=+[\]{};':",.<>/?|])[a-zA-Z0-9`~!@#$%^&*()\-_=+[\]{};':",.<>/?|]{10,20}$/
      );
  };

  const isPasswordValid = passwordValidation(password);

  return (
    <form>
      <input
        type="text"
        onChange={(e) => setPassword(e.target.value)}
        maxlength="20"
      />
      <input type="submit" disabled={!isPasswordValid} />
    </form>
  );
};

// [3-5]

// 굉장히 느리게 랜더링 되는 컴포넌트 <Delay />를 포함한 페이지가 있습니다.

// 해당 페이지의 input[type="text"]과 input[type="number"]이 현재 onChange를 통해 제어되고 있습니다.

// 사용자가 input[type="text"]의 값을 변경할때마다 "text"가 변하면서 불필요하게 Delay 컴포넌트가 랜더링 되서 성능 저하가 일어납니다.

// 이 페이지의 성능을 개선할 수 있는 방법을 활용해주세요. 정답은 다양합니다.

// [예]

import { useState } from "react";

const Delay = ({ num }) => {
  const complex = (num) => {
    let m = num;
    let j = 0;
    for (let i = 0; i < 10000; i++) {
      j += i;
    }
    for (let k = 0; k < j; k++) {
      m += k;
    }
    return m;
  };
  const a = complex(num);
  return <div>{a}</div>;
};

const Rendering = () => {
  const [text, setText] = useState("");
  const [num, setNum] = useState("0");
  const onChangeText = (e) => {
    const { value: text } = e.target;
    setText(text);
  };

  const debounce = (callback, timeout) => {
    let timer;

    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        callback(...args);
      }, timeout);
    };
  };

  const useInput = (setValue) => {
    const handleOnChange = debounce((e) => {
      setValue(e.target.value);
    }, 300);

    return handleOnChange;
  };

  const onChangeNum = useInput(setNum);

  return (
    <div>
      <div>
        <input type="text" value={text} onChange={onChangeText} />
      </div>
      <div>
        <input type="number" value={num} onChange={onChangeNum} />
        <Delay num={+num} />
      </div>
    </div>
  );
};

export default Rendering;

function isPalindrome(str) {
  str.trim();
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    let left = str[i];
    let right = str[str.length - 1 - i];

    if (left === " " || right === " ") {
      continue;
    } else if (left != right) {
      return false;
    }
  }
  return true;
}
