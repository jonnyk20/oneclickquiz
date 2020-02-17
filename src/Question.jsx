import React, { useState, useEffect } from "react";

const Question = ({ question, incrementScore, incrementQuestion }) => {
  const { choices, correct_answer } = question;
  const [isAnswered, setIsAnswered] = useState(false);

  const answerCorrectly = () => console.log("YES");
  const answerIncorrectly = () => console.log("NO");

  const answerQuestion = i => {
    if (isAnswered) return;
    setIsAnswered(true);
    if (i === correct_answer) {
      answerCorrectly();
      incrementScore();
      return;
    }

    answerIncorrectly();
  };

  const moveToNexQuestion = () => {
    incrementQuestion();
    setIsAnswered(false);
  };

  return (
    <div>
      <div>{choices[correct_answer].name}</div>
      <ul>
        {choices.map(({ legs }, i) => (
          <li key={legs} onClick={() => answerQuestion(i)}>
            {legs}
          </li>
        ))}
      </ul>
      {isAnswered && <button onClick={moveToNexQuestion}>Next</button>}
    </div>
  );
};

export default Question;
