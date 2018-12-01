# This file is intended to hold all schema information related to XMI itself. e.g. XMI-2.1
#
# Copyright (C) 2018 Logan Campos - @binaryflesh
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


'''
    Param/Event/State
  /    /      \      \
<e>--_Components_--><phook>
\    /           \    /
XMI-$VER----------Groups
'''

class XMI_10(Base):
    __table__ = "xml10"

    id = Column(Integer, primary_key=True)
    """
    Model_Management -> {Package, Model}
    XMI:content
    UML:Diagram -> {owner}
    UML:Uml1SemanticModelBridge -> {element}
    Behavioral_Elements -> {State_Machines, Collaborations, Common_Behavior, Use_Cases}
        State_Machines.StateMachine -> {context, top, transitions}
        State_Machines.SignalEvent
        State_Machines.Transition -> {source, target, effect, guard}
        Collaborations.Collaboration
        Collaboration.ClassifierRole -> {base}
        State_Machines.CompositeState -> {subvertex}
        State_Machines.State
        State_Machines.Pseudostate -> {kind}
        State_Machines.Finalstate
        State_Machines.StateVertex -> {outgoing, incoming}
        Common_Behavior.Action -> {script}
        Use_Cases.Actor
    Foundation -> { Core, Data_Types, ModelElement, Extension_Mechanisms}
        Core.Namespace -> {ownedElement}
        Core.ModelElement -> {name}
        Core.Class
        Core.StructuralFeature -> {multiplicity, type}
        Core.Attribute -> {initialValue}
        Core.DataType
        Core.Classifier -> {feature}
        Core.Association
        Core.AssociationClass
        Core.AssociationEnd -> {aggregation, type}
        Core.Operation
        Core.Parameter -> {defaultValue}
        Core.Generalization -> {child, parent}
        Core.GeneralizableElement -> {isAbstract}
        Core.ModelElement -> {taggedValue}
        Core.Interface
        Core.Abstraction
        Core.Dependency -> {client, supplier}
        Data_Types.Expression -> {body, }
        Data_Types.Expression.MultiplicityRange -> {lower, upper}
        Data_Types.BooleanExpression
        Data_Types.ActionExpression
        Data_Types.Expression -> {body}
        Extension_Mechanisms -> {TaggedValue, Stereotype}
        Extension_Mechanisms.TaggedValue -> {tag, value}
        Extension_Mechanisms.Stereotype -> {extendedElement}
    """