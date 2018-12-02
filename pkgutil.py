# This file is meant for package maintainers to generate data sources to be distributed in the TBD package.
# Copyright (C) 2018 Logan Campos - @binaryflesh
# ORM-related imports
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# WIP
'''        o
     _____[ ]_____
    /             \
    Param/Event/State
  /    /      \      \
<e>--_Components_--><ph>
\    /           \    /
XMI-$VER---[ ]---Groups
            i
'''         
class Components(Base):
    __table__ = "components"
    id = Column(Integer, primary_key=True)
    uid = Column(String, nullable=False)
    groupid = Column()

class XMI_10(Base):
    __table__ = "xml10"
    id = Column(Integer, primary_key=True)
    """
    Model_Management -> {Package, Model}
    XMI:content
    UML:Diagram -> {owner}
    UML:Uml1SemanticModelBridge -> {element}
    Behavioral_Elements -> {State_Machines, Collaborations, Common_Behavior, Use_Cases}
    Behavioral_Elements.State_Machines.StateMachine -> {context, top, transitions}
    Behavioral_Elements.State_Machines.SignalEvent
    Behavioral_Elements.State_Machines.Transition -> {source, target, effect, guard}
    Behavioral_Elements.Collaborations.Collaboration
    Behavioral_Elements.Collaboration.ClassifierRole -> {base}
    Behavioral_Elements.State_Machines.CompositeState -> {subvertex}
    Behavioral_Elements.State_Machines.State
    Behavioral_Elements.State_Machines.Pseudostate -> {kind}
    Behavioral_Elements.State_Machines.Finalstate
    Behavioral_Elements.State_Machines.StateVertex -> {outgoing, incoming}
    Behavioral_Elements.Common_Behavior.Action -> {script}
    Behavioral_Elements.Use_Cases.Actor
    Foundation -> { Core, Data_Types, ModelElement, Extension_Mechanisms}
    Foundation.Core.Namespace -> {ownedElement}
    Foundation.Core.ModelElement -> {name}
    Foundation.Core.Class
    Foundation.Core.StructuralFeature -> {multiplicity, type}
    Foundation.Core.Attribute -> {initialValue}
    Foundation.Core.DataType
    Foundation.Core.Classifier -> {feature}
    Foundation.Core.Association
    Foundation.Core.AssociationClass
    Foundation.Core.AssociationEnd -> {aggregation, type}
    Foundation.Core.Operation
    Foundation.Core.Parameter -> {defaultValue}
    Foundation.Core.Generalization -> {child, parent}
    Foundation.Core.GeneralizableElement -> {isAbstract}
    Foundation.Core.ModelElement -> {taggedValue}
    Foundation.Core.Interface
    Foundation.Core.Abstraction
    Foundation.Core.Dependency -> {client, supplier}
    Foundation.Data_Types.Expression -> {body, }
    Foundation.Data_Types.Expression.MultiplicityRange -> {lower, upper}
    Foundation.Data_Types.BooleanExpression
    Foundation.Data_Types.ActionExpression
    Foundation.Data_Types.Expression -> {body}
    Foundation.Extension_Mechanisms -> {TaggedValue, Stereotype}
    Foundation.Extension_Mechanisms.TaggedValue -> {tag, value}
    Foundation.Extension_Mechanisms.Stereotype -> {extendedElement}
    """

class XMI_11(Base):
    id = Column(Integer, primary_key=True)
    """
    UML:ModelElement -> {name}
    UML:Namespace -> {ownedElement}
    UML:Model
    UML:Class
    UML:Package
    UML:Attribute -> {initialValue}
    UML:DataType
    UML:Classifier -> {feature}
    UML:StructuralFeature -> {multiplicity, type}
    UML:Association -> {aggregation}
    UML:AssociationEnd -> {type, participant}
    UML:Operation
    UML:Parameter -> {defaultValue}
    UML:MultiplicityRange -> {lower, upper}
    UML:Generalization -> {child, parent}
    UML:Expression
    UML2:OpaqueExpression
    UML:TagDefinition
    UML:ModelElement -> {taggedValue, stereotype}
    UML:TaggedValue -> {tag, value}
    UML:Stereotype
    UML:GeneralizableElement -> {isAbstract}
    UML:Interface
    UML:Abstraction
    UML:Dependency -> {client, supplier}
    UML:AssociationClass
    UML:BooleanExpression
    UML2:OpaqueExpression
    UML:StateMachine -> {context, top, transitions}
    UML2:StateMachine 
    UML:CompositeState -> {subvertex}
    UML:SimpleState
    UML2:State
    UML:Pseudostate -> {kind}
    UML2:Pseudostate -> {kind}
    UML:FinalState
    UML:StateVertex -> {outgoing, incoming}
    UML2:Vertex -> {outgoing, incoming}
    UML:Transition -> {target, source, effect, guard}
    UML2:Transition -> {target, source, effect, guard}
    UML2:BehavioredClassifier -> {ownedBehavior}
    UML:Action -> {script}
    UML2:OpaqueBehavior -> {body}
    UML:ActionExpression -> {body}
    UML:Diagram -> {owner}
    UML:Uml1SemanticModelBridge -> {element}
    UML:Actor
    UML2:TypedElement -> {type}
    Behavioral_Elements -> {Collaborations}
    Behavioral_Elements.Collaborations -> {Collaboration}
    """