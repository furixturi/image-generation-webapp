import { ChangeEvent, useState } from "react";

import {
  Box,
  Button,
  Container,
  Heading,
  Image,
  Input,
  InputGroup,
  InputRightElement,
  Spinner,
} from "@chakra-ui/react";

function App() {
  // states
  const [prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [imgSrc, setImgSrc] = useState("https://picsum.photos/640");

  // event handlers
  const onInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setPrompt(e.target.value);
  };

  const onButtonClick = async () => {
    setIsLoading(true);
    try {
      const response = await (
        await fetch(`http://127.0.0.1:8000/generate-image?prompt=${prompt}`)
      ).json();
      console.log(response);
    } catch (err: any) {
      // catch any runtime error
      console.log(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container maxWidth={"2xl"} marginTop={30} centerContent>
      <Heading margin={8}>Image Generator</Heading>
      <InputGroup>
        <Input
          pr="4.5rem"
          value={prompt}
          placeholder="Enter your prompt"
          onChange={onInputChange}
        />
        <InputRightElement width={"6rem"}>
          <Button onClick={onButtonClick} isDisabled={isLoading}>
            Generate!
          </Button>
        </InputRightElement>
      </InputGroup>
      {isLoading ? (
        <Spinner
          thickness="4px"
          speed="0.65s"
          emptyColor="gray.200"
          color="blue.500"
          size="xl"
          marginTop={6}
        />
      ) : imgSrc ? (
        <Box boxSize={"l"} marginTop={5}>
          {/* <Image src={`data:image/png;base64,${imageData}`} /> */}
          <Image src={imgSrc} />
        </Box>
      ) : null}
    </Container>
  );
}

export default App;
