from abc import ABC, abstractmethod
from pydantic import BaseModel

class AbstractResponse(BaseModel, ABC):
  description: str
  content_type: str
  message: str

  @abstractmethod
  def custom_response() -> dict:
    pass

class Response(AbstractResponse):
  def custom_response(self) -> dict:
    return {
      "description": self.description,
      "content": {
        self.content_type: {
          "example": {
            "description": self.description,
            "message": self.message
          }
        }
      }
    }