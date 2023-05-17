const fs = require("fs");
const { Deepgram } = require("@deepgram/sdk");

const deepgramApiKey = "8192ec1755dc5fb2683a51371f2a34badd0bba29";
const file = "./Assets/Convo-transcript.mp3";
const mimetype = "mp3";

const deepgram = new Deepgram(deepgramApiKey);
if (file.startsWith("http")) {
  source = {
    url: file,
  };
} else {
  const audio = fs.readFileSync(file);

  source = {
    buffer: audio,
    mimetype: mimetype,
  };
  deepgram.transcription
    .preRecorded(source, {
      punctuate: true,
      model: "conversationalai",
    })
    .then((response) => {
      console.dir(response, { depth: null });
      console.log("line 27");
      fs.writeFileSync(
        "./Assets/Transcript1.txt",
        response.results.channels[0].alternatives[0].transcript,
        { encoding: "utf8", flag: "w" }
      );
    })
    .catch((err) => {
      console.log(err);
    });
}
