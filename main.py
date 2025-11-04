from fastapi import FastAPI, HTTPException

from agents import Generator
from orm_schemas.persona import PersonaRequest


app = FastAPI()





@app.post("/generate_scenario")
async def generate_story(req: PersonaRequest):
    try:
        # Generate scenario
        story_data = Generator.generate_persona_scenario(req.persona)
        if story_data.get("status") == "failed":
            raise ValueError(story_data.get("details", "Story generation failed"))

        # subscenario
        substory_data = Generator.generate_persona_subscenario(story_data["persona_scenario"], req.persona)
        if substory_data.get("status") == "failed":
            raise ValueError(substory_data.get("details", "Substory generation failed"))

        #final output
        return {
            #"persona": req.persona, (if want to show persona here also)
            "Overall_story": story_data["Overall_story"],
            "persona_scenario": story_data["persona_scenario"],
            "persona_subscenario": substory_data["persona_subscenario"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

