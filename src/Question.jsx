import React, { useState } from "react";
import Image from "./Image";

const states = {
  UNANSWERED: "UNANSWERED",
  CORRECT: "CORRECT",
  INCORRECT: "INCORRECT"
};

const Question = ({ question, incrementScore, incrementQuestion }) => {
  const { choices, correct_answer } = question;
  const [state, setState] = useState(states.UNANSWERED);
  const answerCorrectly = () => console.log("YES");
  const answerIncorrectly = () => console.log("NO");

  const answerQuestion = i => {
    if (isAnswered) return;
    if (i === correct_answer) {
      setState(states.CORRECT);
      answerCorrectly();
      incrementScore();
      return;
    }

    setState(states.INCORRECT);
    answerIncorrectly();
  };

  const moveToNexQuestion = () => {
    incrementQuestion();
    setState(states.UNANSWERED);
  };

  const isAnswered = state !== states.UNANSWERED;
  const isAnsweredCorrectly = state === states.CORRECT;

  const answerFeedback = isAnsweredCorrectly ? "Correct!" : "Wrong!";

  console.log("choices[correct_answer]", choices[correct_answer]);
  console.log("choices[correct_answer]", choices);
  console.log("choices[correct_answer]", correct_answer);

  return (
    <div className="question">
      <div className="question__image-container">
        {choices.map(({ image_url, name }, i) => (
          <Image
            key={image_url}
            answerQuestion={answerQuestion}
            i={i}
            image_url={image_url}
            name={name}
            isCorrect={i === correct_answer}
            isAnswered={isAnswered}
          />
        ))}
      </div>
      <div className="question__prompt">
        {!isAnswered ? (
          `Find the ${choices[correct_answer].name}`
        ) : (
          <>
            {answerFeedback}
            <button onClick={moveToNexQuestion}>Next</button>
          </>
        )}
      </div>
    </div>
  );
};

export default Question;
