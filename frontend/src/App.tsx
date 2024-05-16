import { Button } from "@chakra-ui/button";
import { Center } from "@chakra-ui/layout";
import { main } from "./chat-gpt";

function App() {
  return (
    <Center>
      <Button onClick={main}>meow</Button>
    </Center>
  );
}

export default App;
