from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class FintechUxResearch():
    """Research crew với 4 agents + revision loop"""

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
            output_file='output/02_insight_v1.md'
        )
    
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            output_file='output/03_review_v1.md'
        )
    
    @task
    def revision_task(self) -> Task:
        return Task(
            config=self.tasks_config['revision_task'],
            output_file='output/04_insight_v2.md'
        )
    
    @task
    def re_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['re_review_task'],
            output_file='output/05_review_v2.md'
        )
    
    @task
    def visualize_task(self) -> Task:
        return Task(
            config=self.tasks_config['visualize_task'],
            output_file='output/06_final_report.md'
        )

    # ========== CREW ==========
    
    @crew
    def crew(self) -> Crew:
        """Pipeline với revision loop"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )