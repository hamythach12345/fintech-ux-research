from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class FintechUxResearch():
    """FintechUxResearch crew với 4 agents: Researcher, Synthesizer, Reviewer, Visualizer"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ========== AGENTS ==========
    
    @agent
    def ux_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['ux_researcher'],
            verbose=True
        )

    @agent
    def insight_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['insight_synthesizer'],
            verbose=True
        )
    
    @agent
    def quality_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_reviewer'],
            verbose=True
        )
    
    @agent
    def visualizer(self) -> Agent:
        return Agent(
            config=self.agents_config['visualizer'],
            verbose=True
        )

    # ========== TASKS ==========
    
    @task
    def user_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_research_task'],
            output_file='output/01_raw_research.md'
        )

    @task
    def synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['synthesis_task'],
            output_file='output/02_insight_draft.md'
        )
    
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            output_file='output/03_review_report.md'
        )
    
    @task
    def visualize_task(self) -> Task:
        return Task(
            config=self.tasks_config['visualize_task'],
            output_file='output/04_final_report.md'
        )

    # ========== CREW ==========
    
    @crew
    def crew(self) -> Crew:
        """Creates the FintechUxResearch crew - sequential pipeline"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )