import { Center } from "@chakra-ui/layout";
import { Button } from "@chakra-ui/react";
import { useCallback, useState } from "react";



function App() {
  const [insult, setInsult] = useState<string>("");
  const getInsult = useCallback(async () => {
    return (await fetch("https://localhost:5000/insult")).text();
  }, [setInsult]);
  return (
    <Center>
      <p>{insult}</p>
      <Button
        onClick={() =>
          getInsult()
            .then((insult) => setInsult(insult))
            .catch(console.error)
        }
      >
        Insult me!
      </Button>
    </Center>
  );
}

export default App;
